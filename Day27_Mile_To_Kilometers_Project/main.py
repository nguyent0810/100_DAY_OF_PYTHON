from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def calculate():
    miles_value = int(my_entry.get())
    km_value = miles_value * 1.6
    result_label.config(text=round(km_value, 2))

my_entry = Entry()
my_entry.grid(column=1, row=0)
my_entry.config(width=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

equal_label = Label(text="Is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=2)
window.mainloop()
