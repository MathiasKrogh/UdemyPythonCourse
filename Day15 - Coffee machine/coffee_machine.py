import os

def clear():
    os.system('cls')

flavours = {
    "espresso": {
        "Water": 50,
        "Milk": 0,
        "Coffee": 18,
        "Money": 1.5
    },
    "latte": {
        "Water": 200,
        "Milk": 150,
        "Coffee": 24,
        "Money": 2.5
    },
    "cappuccino": {
        "Water": 250,
        "Milk": 100,
        "Coffee": 24,
        "Money": 3.0
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0.0
}

def report():
    print(f"Water: {resources["Water"]}ml")
    print(f"Milk: {resources["Milk"]}ml")
    print(f"Coffee: {resources["Coffee"]}g")
    print(f"Money: ${resources["Money"]}")

def check_resources(flavour):
    sufficient = True
    problem = ""
    for i in flavour:
        if i == "Money": continue
        if resources[i] < flavour[i]:
            sufficient = False
            problem = i.lower()
    return sufficient, problem

def brew(flavour):
    for i in resources:
        if i == "Money": continue
        resources[i] -= flavour[i]

def insert_coins(flavour, choice):
    price = flavour["Money"]
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.10
    nickles = int(input("How many nickles?: "))*0.05
    pennies = int(input("How many pennies?: "))*0.01
    money = quarters + dimes + nickles + pennies
    if price <= money:
        brew(flavour)
        resources["Money"] += price
        print(f"Here is ${round(money - price, 2)} in change.")
        print(f"Here is your {choice} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


if __name__ == "__main__":
    clear()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            break
        elif choice == "report":
            report()
        elif choice in flavours:
            valid, problem = check_resources(flavours[choice])
            if valid:
                print("Please insert coins.")
                insert_coins(flavours[choice], choice)
            else:
                print(f"Sorry, there is not enough {problem}.")
        else:
            print("Not a valid option. ")
            