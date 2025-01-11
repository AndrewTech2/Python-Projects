import time

not_available = False
menu_dict = {
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
key_dict = {'1': 'espresso', "2": 'latte', "3": 'cappuccino'}


while True:
    menu = input("""What would you like to do?
1. Buy an espresso
2. Buy a latte
3. Buy a cappuccino
4. View report
> """).lower()
    print()
    if menu == "off":
        print("Machine turned off!")
        exit()
    elif menu == "4":
        print("Machine report:")
        for x in resources:
            if x == 'money':
                print(x.capitalize(), f'${resources[x]}', sep=": ")
            elif x == "coffee":
                print(x.capitalize(), f'{resources[x]} g', sep=": ")
            else:
                print(x.capitalize(), f"{resources[x]} ml", sep = ": ")
        cont = input("Press any key to continue > ")
        print("\n" * 100)
    elif menu == "1" or menu == '2' or menu == '3':
        for x in menu_dict[key_dict[menu]]['ingredients']:
            if resources[x] < menu_dict[key_dict[menu]]['ingredients'][x]:
                not_available = True
                missing = x
                break
        if not_available:
            print(f"Not available. There is not enough {missing}.")
            not_available = False
        else:
            cost = menu_dict[key_dict[menu]]['cost']
            print(f"Cost: ${cost}")
            try:
                quarters = int(input("Number of quarters > "))
                dimes = int(input("Number of dimes > "))
                nickles = int(input("Number of nickles > "))
                pennies = int(input("Number of pennies > "))
                print()
            except ValueError:
                print("Not a number.")
            else:
                user_sum = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                if user_sum < cost:
                    print("Not enough money. Money is being refunded.")
                else:
                    if user_sum > cost:
                        print(f"Here's your change: ${user_sum - cost}.")
                    print(f"Here's your {key_dict[menu]} ☕.")
                    resources['money'] += cost
                    for x in resources:
                        try:
                            resources[x] -= menu_dict[key_dict[menu]]['ingredients'][x]
                        except KeyError:
                            continue
        time.sleep(2)
        print("\n" * 100)
    else:
        print("\n" * 100)