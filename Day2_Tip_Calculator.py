# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 =

from tkinter import *
import tkinter
from tkinter import font
window = Tk()
window.title("Tip Generator")
window.config(padx=20, pady=20)
def calculate_bill():
    percent_tip_value = int(percent_tip_entry.get())
    total_bill = int(bill_q_entry.get())
    split_people = int(split_people_entry.get())
    total_tip = 1 + percent_tip_value / 100
    total_money = total_bill * total_tip
    money_each_people = round(total_money / split_people, 2)
    calculate_label["text"] = f"Each person should pay ${money_each_people}"

wc_label = Label(text="Welcome to the tip calculator", font=("Courier", 18, "bold"))
wc_label.pack()
bill_q_label = Label(text="What was the total bill?", font=("Courier", 12))
bill_q_label.pack()
bill_q_entry = Entry()
bill_q_entry.pack()
percent_tip_label = Label(text="What percentage tip would you like to give?", font=("Courier", 12))
percent_tip_label.pack()
percent_tip_entry = Entry()
percent_tip_entry.pack()
split_people_label = Label(text="How many people to split the bill?",font=("Courier", 12))
split_people_label.pack()
split_people_entry = Entry()
split_people_entry.pack()
calculate_button = Button(text="Calculate", command=calculate_bill, padx=10, pady=10)
calculate_button.pack()
calculate_label = Label(font=("Courier", 20, "bold"))
calculate_label.pack()
window.mainloop()


# total_tip = 1 + int(percentage_tip) / 100

# total_money = float(total_bill) * total_tip
# money_each_people = total_money / int(split_people)
# final_amount = round(money_each_people, 2)
# final_amount = "{:.2f}".format(money_each_people)
# print(f"Each person should pay: ${final_amount}")