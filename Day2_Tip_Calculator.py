# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 =
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
percentage_tip = input("What percentage tip would you like to give? ")
total_tip = 1 + int(percentage_tip) / 100
split_people = input("How many people to split the bill? ")

total_money = float(total_bill) * total_tip
money_each_people = total_money / int(split_people)
final_amount = round(money_each_people, 2)
final_amount = "{:.2f}".format(money_each_people)
print(f"Each person should pay: ${final_amount}")