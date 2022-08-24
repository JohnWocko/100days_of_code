''' Makes 3 types of coffee 

    Print report
    Check Resources
    Process coins
    Check transaction state
    Make coffee
        Deduct resources
        increase machine balance

'''

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
}


def get_user_choice():
    try:
        choice = input('Please select a coffee type:☕\n\n☕ - Cappuccino (c)\n☕ - Latte (l)'
        + '\n☕ - Espresso (e)\n')

        if choice.lower() not in 'cle':
            print('Input not recognised ...\nTry Again.')
            get_user_choice()
        elif choice.lower() == 'c':
            return {'cappuccino': MENU['cappuccino']}
        elif choice.lower() == 'l':
            return MENU['latte']
        elif choice.lower() == 'e': 
            return MENU['espresso']   
        return choice
    except:
        print('Input not recognised ...\nTry Again.')
        print(get_user_choice())


user_choice = get_user_choice()
print(user_choice.keys())