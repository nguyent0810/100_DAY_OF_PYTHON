MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

money = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "penny": 0.01
}
is_continue = True
def update_based_resource(user_input):
    resources["money"] += MENU[user_input]["cost"]
                
    
def check_user_insert_coint(user_input):
    print("Please insert coins.")
    result = 0
    for k in money:
        quantity = float(input(f"How many {k}: "))
        result = result + (money[k] * quantity)
    if result > MENU[user_input]["cost"]:
        remaining = result - MENU[user_input]["cost"]
        print(f"Here is ${round(remaining, 2)} in change.")
        print(f"Here is your {user_input}☕. Enjoy")
        update_based_resource(user_input)
    elif result == MENU[user_input]["cost"]:
        print(f"Here is your {user_input}☕. Enjoy")
        update_based_resource(user_input)
    else:
        print("Sorry there is not enough money")

def check_resource(drink, resource, based_resources):
    needed_resource = MENU[drink]["ingredients"][resource]
    if resource in MENU[drink]["ingredients"]:
        needed_resource = MENU[drink]["ingredients"][resource]
    else: 
        needed_resource = 0
    
    if resources[resource] - needed_resource < 0: 
        print(f"Sorry there is not enough {resource}")
        return False
    # else:
    #     based_resources[resource] -= needed_resource

def check_user_input(user_input, based_resources): 
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        for k in MENU[user_input]["ingredients"]:
            if(check_resource(user_input, k, based_resources)) == False:
                return coffee_machine()
        check_user_insert_coint(user_input)
        resources["money"] -= MENU[user_input]["cost"]
    
    elif user_input == "report":
        for item in resources:
            if item == "money":
                print(f"{item.title()}: ${resources[item]}")
            elif item == "coffee":
                print(f"{item.title()}: {resources[item]}g")
            else:
                print(f"{item.title()}: {resources[item]}ml")
    elif user_input == "off":
        return
    coffee_machine()
def coffee_machine():
    choice = input("What would you like? (espresso/ latte/ cappuccino: ")
    check_user_input(choice, resources)

coffee_machine()
    