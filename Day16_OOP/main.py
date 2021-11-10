from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
list_drink = menu.get_items()

is_on = True

while is_on:
    choice = input(f"What would you like? ({list_drink})")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:    
        choice_item = menu.find_drink(choice)
        is_resources_sufficient = coffee_maker.is_resource_sufficient(choice_item)
        if is_resources_sufficient:
                
        else:
    
    
    
