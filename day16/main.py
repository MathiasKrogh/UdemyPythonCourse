from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ")
        
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue
        drink = menu.find_drink(choice)
        if drink != None:
            if coffee_maker.is_resource_sufficient(drink):
                valid_payment = money_machine.make_payment(drink.cost)
                if valid_payment:
                    coffee_maker.make_coffee(drink)