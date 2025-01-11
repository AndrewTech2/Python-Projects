from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    print("What do you want to get?")
    print(menu.get_items())
    choice = input("> ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        input("Type anything to continue > ")
    if choice in menu.get_items().split("/"):
        drink = menu.find_drink(choice)
        cost = drink.cost
        if not coffee_maker.is_resource_sufficient(drink):
            print("Resources not available.")
            time.sleep(2)
        else:
            print(f"The cost is {cost}.")
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(drink)
                time.sleep(2)
            else:
                print("Transaction failed. Not enough. Money is being refunded.")
                time.sleep(2)
    else:
        print("Not in the list.")
        time.sleep(2)
    print("\n" * 100)