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

def check_water(required_resources):
    return (resources['water'] - required_resources['ingredients']['water'] ) >= 0

def check_milk(required_resources):
    return (resources['milk'] - required_resources['ingredients']['milk'] ) >= 0

def check_coffee(required_resources):
    return (resources['coffee'] - required_resources['ingredients']['coffee'] ) >= 0

def check_resources(required_resources):
    return check_coffee(required_resources) and check_milk(required_resources) and check_water(required_resources)

def update_resources(required_resources):
    if check_resources(required_resources):
        resources['water'] -= required_resources['ingredients']['water'] 
        resources['milk'] -= required_resources['ingredients']['milk'] 
        resources['coffee'] -= required_resources['ingredients']['coffee']
        return f"£{required_resources['cost']}"
    else:
        print('Insufficient Resources\n£0.00')

def get_user_choice():
    try:
        
        choice = input('Please select a coffee type:☕\n\n☕ - Cappuccino (c)\n☕ - Latte (l)'
        + '\n☕ - Espresso (e)\n')

        if choice.lower() not in 'cle':
            print('Input not recognised ...\nTry Again.')
            return get_user_choice()
        elif choice.lower() == 'c':
            return ('cappuccino', MENU['cappuccino'])
        elif choice.lower() == 'l':
            return ('latte', MENU['latte'])
        else:
            return ('espresso', MENU['espresso'])   

    except:
        print('Input not recognised ...\nTry Again.')
        return get_user_choice()


user_choice = get_user_choice()
print(user_choice[0],user_choice[1], update_resources(user_choice[1]))
print(resources)
update_resources(user_choice[1])
print(resources)
