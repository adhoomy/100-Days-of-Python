from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

choices = ["espresso", "latte", "cappuccino", "off", "report"]

power = True
while power:
    choices = menu.get_items()
    choice = input(f"What would you like? ({choices}): ")
    if choice == "off":
        power = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            can_afford = money_machine.make_payment(drink.cost)
            if can_afford:
                coffee_maker.make_coffee(drink)
            if not can_afford:
                print("Sorry, that's not enough money. Money has been refunded.")
        if not can_make:
            coffee_maker.is_resource_sufficient(drink)
