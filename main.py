from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

power_state = True

while power_state:
    options = menu.get_items()
    prompt_answer = input(f"What would you like? ({options}): ")
    if prompt_answer == "off":
        power_state = False
    elif prompt_answer == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_ordered = menu.find_drink(prompt_answer)
        if coffee_maker.is_resource_sufficient(drink_ordered) and money_machine.make_payment(drink_ordered.cost):
            coffee_maker.make_coffee(drink_ordered)
