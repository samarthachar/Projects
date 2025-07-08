MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
total = 0
def check_resources():
    for i in ["milk", "water", "coffee"]:
        if MENU[inp]["ingredients"][i] >= resources[i]:
            pass
        else:
            return f"Sorry there is not enough {i}"
    return None
def reduce_resources():
    for i in ["milk", "water", "coffee"]:
        resources[i] -= MENU[inp]["ingredients"][i]
def  espresso():
    check_resources()

def process_coins():
    quarters = 25 * int(input("How many quarters?: "))
    dimes = 10 * int(input("How many dimes?: "))
    nickles = 5 * int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    global total
    total = (quarters + dimes + nickles + pennies) / 100

def main_code():
    if inp not in MENU:
        return "Does not exist: ERROR"
    check_resources()
    process_coins()
    if total < MENU[inp]["cost"]:
        return "Sorry that's not enough money. Money refunded."
    reduce_resources()
    resources["money"] += MENU[inp]["cost"]
    return f"Here is your ${total - MENU[inp]["cost"]} in change.\nHere is your {inp} ☕️. Enjoy!"



on = True
while on:
    inp = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if inp == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif inp == "off":
        on = False
    else:
        print(main_code())