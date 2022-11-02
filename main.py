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

earnings = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink_ingredients):
    """Returns true if item for required drink is available to make the drink and false if not """
    for item in drink_ingredients:
        if drink_ingredients[item] <= resources[item]:
            return True
        elif drink_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item} to make your drink.")
            return False


def check_transaction(user_payment, drink_cost):
    """Return if the payment is accepted or false if money is not enough."""
    if user_payment >= drink_cost:
        change = round(user_payment - drink_cost, 2)
        global earnings
        earnings += drink_cost
        print(f"Your change is ${change}")
        return True
    else:
        print(f"Sorry your amount of ${user_payment} is not enough for the drink selected.")
        return False


def brewing_drink(type_of_drink, drink_ingredients):
    """Function subtracts the user input drink resources from the machine resources. Also prints
    the drink the user wants"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Your {type_of_drink}☕ is brewed. Enjoy and Have a great day!!")


def coffee_machine():
    brewing = True
    while brewing:
        decision = input("What would you like to drink? (espresso / latte / cappuccino): ")

        if decision == 'off':
            print("Machine is off!")
            brewing = False
        elif decision == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Earnings: ${earnings}")
        else:
            coffee_drink = MENU[decision]
            if check_resources(coffee_drink['ingredients']):
                print("Please insert coins")
                qt = int(input("How many quarters?: ")) * 0.25
                di = int(input("How many dimes?: ")) * 0.10
                nl = int(input("How many nickles?: ")) * 0.05
                pn = int(input("How many pennies?: ")) * 0.01
                total_payment = qt + di + nl + pn
                if check_transaction(total_payment, coffee_drink['cost']):
                    brewing_drink(decision, coffee_drink['ingredients'])


coffee_machine()
