
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
    "money" : 0
}







def insert_coins() :
    print("Please insert coins")
    coins = {"quarter": 0, "dime": 0, "nickel": 0, "penny": 0}
    for key, value in coins.items() :
        count = int(input(f"How many {key}?"))
        coins[key] = count
    return coins


def payment(coins ):
    total = 0.25 * coins['quarter'] + 0.10 * coins['dime'] + 0.05* coins['nickel'] + 0.01*coins['penny']
    return total
def make_coffe(choice_data):
    for key  in choice_data["ingredients"]:
        if resources[key] < choice_data["ingredients"][key]:
            print("You can't make a coffe!")
            return
    user_money = insert_coins()
    if(payment(user_money) < MENU[choice]["cost"]):
        print("You don't have enough money to make a coffe!")
        return
    else :
        resources["money"] += MENU[choice]["cost"]
        if(payment(user_money) > MENU[choice]["cost"]):
            print(f"Here is ${float(payment(user_money) - MENU[choice]["cost"]):.2f} in change")
        for key in choice_data["ingredients"]:
            resources[key] -= choice_data["ingredients"][key]
        return 1





is_coffee_machine_on = True

while is_coffee_machine_on:
    choice = input("What would you like?")
    if(choice == 'report'):
        print(resources)
    elif(choice == 'off'):
        print("Coffee Machine is off")
        is_coffee_machine_on = False
    elif choice in MENU:
        choice_data = MENU[choice]
        if make_coffe(choice_data) :
            print(f"Here is your {choice}")











