from tkinter import *
from tkinter import font

def band_name_generator():
    city = city_entry.get()
    pet = pet_entry.get()
    band_label["text"] = f"Your band name could be {city} {pet}"
#1. Create a greeting for your program.
window = Tk()
window.title("Band Name Generator")
window.config(padx=20, pady=20)
welcome_label = Label(text="Welcome to the Band Name Generator")
welcome_label.config(font=("Courier", 20, "bold"))
welcome_label.pack()
#2. Ask the user for the city that they grew up in.
city_q_label = Label(text="What's name of the city you grew up in?")
city_q_label.config(font=("Courier", 14))
city_q_label.pack()
city_entry = Entry(width=50)
city_entry.config(font=("Courier", 14))
city_entry.pack()
#3. Ask the user for the name of a pet.
pet_q_label = Label(text="What's your pet's name?")
pet_q_label.config(font=("Courier", 14))
pet_q_label.pack()
pet_entry = Entry(width=50)
pet_entry.config(font=("Courier", 14))
pet_entry.pack()
#4. Combine the name of their city and pet and show them their band name.
generator_button = Button(text="Generator", command=band_name_generator)
generator_button.config(font=("Courier", 14))
generator_button.pack(padx=10, pady=10)
generator_button.pack()

band_label = Label()
band_label.config(font=("Courier", 14))
band_label.pack()


window.mainloop()
#print("Your band name could be " + your_city_name + " " + your_pet_name)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/