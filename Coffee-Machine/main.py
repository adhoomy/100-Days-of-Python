import data


def print_resources(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(choice, resources, menu):
    enough = True
    for k, v in menu[choice]['ingredients'].items():
        if resources[k] < v:
            print(f"Sorry, there is not enough {k}.")
            enough = False
    return enough


def insert_coins():
    quarters = int(input("Insert how many quarters?: "))
    dimes = int(input("Insert how many dimes?: "))
    nickles = int(input("Insert how many nickles?: "))
    pennies = int(input("Insert how many pennies?: "))
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01


def check_money(amount, menu, resources, choice):
    if amount < menu[choice]['cost']:
        print("Sorry, that's not enough money. Money has been refunded.")
        return False
    else:
        if amount > menu[choice]['cost']:
            print(f"Here is ${amount - menu[choice]['cost']} in change.")
        resources['money'] += menu[choice]['cost']
        return True


def make_drink(choice, resources, menu):
    for k in menu[choice]['ingredients']:
        resources[k] -= menu[choice]['ingredients'][k]
    print(f"Here is your {choice}, enjoy!")


power = True
while power:
    choice = (input("What would you like?: ")).lower()
    while choice not in data.inputs:
        choice = (input("Please enter a valid request: ")).lower()
    if choice == "off":
        power = False
    if choice == "report":
        print_resources(data.resources)
    if choice != "off" and choice != "report":
        able = check_resources(choice, data.resources, data.MENU)
        if able:
            amount = insert_coins()
            enough_money = check_money(amount, data.MENU, data.resources, choice)
            if enough_money:
                make_drink(choice, data.resources, data.MENU)
