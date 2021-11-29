from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for item in range(nr_letters)]
    password_list += [random.choice(symbols) for item in range(nr_symbols)]
    password_list += [random.choice(numbers) for item in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def click_add():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    result = website + ' | ' + user + ' | ' + password + "\n"
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error!","Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user} \nPassword: {password} \nIs it OK to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(result)
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

Label(text="Website:").grid(column=0, row=1)
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
Label(text="Email/Username:").grid(column=0, row=2)
user_entry = Entry(width=40)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "siouxtest05@gmail.com")
Label(text="Password:").grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=click_add)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()