from game_data import data
import random
from art import logo, vs
from replit import clear

def generate_random_account():
    """Returns data of a random account from game_data.py.
    
    :returns: random account from game_data.py.

    """
    return random.choice(data)



def format_data(data):
    '''Formats the data from account into a readable structure that can be compared. '''
    return f"{data['name']} is a {data['description']} from {data['country']}."


def comparison(account_1=0, account_2=0):
    '''Compares two dictionary values representing followers on instagram.
    


    '''
    if type(account_1) == dict and type(account_2) == dict:
        return account_1['follower_count'] >= account_2['follower_count']
    else:
        return False

def get_user_guess(account_1, account_2):
    if type(account_1) == dict and type(account_2) == dict:
        print(
            f'{logo}\n\n\nCompare A:\t{format_data(account_1)} {vs} \nAgainst B:\t{format_data(account_2)}')
        user_guess = input('\nA or B?')

        if user_guess.upper() == 'A':
            print(f"You've chosen {account_1['name']}")
            return comparison(account_1, account_2)

        elif user_guess.upper() == 'B':
            print(f"You've chosen {account_2['name']}")
            return comparison(account_2, account_1)

        else:
            print('Incorrect choice\nTry again:')
            get_user_guess(account_1, account_2)
            return False

    else:
        return False

# Check if user is correct.

def main_loop():
    score = 0
    a = generate_random_account()
    b = generate_random_account()

    while get_user_guess(a, b):
        print(f"{comparison(a, b)}, {a['follower_count']} {b['follower_count']}")
        score += 1
        a = b
        b = generate_random_account()
        print('Score: ', score, '\n',format_data(a), format_data(b))
        clear()

    else:
        print(f"{comparison(a, b)} == {a['name'],a['follower_count']}, {b['name'],b['follower_count']}")
        print(f'Score was: {score}')
        replay = input('Play again? any character except N')

        if replay.upper() != 'N':
            clear()
            main_loop()
        else:
            clear()
            exit()

if __name__ == "__main__":
    main_loop()
