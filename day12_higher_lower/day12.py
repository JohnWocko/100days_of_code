import random
import sys
from game_data import data
from art import logo, vs
from replit import clear

def generate_random_account():
    """
    Returns data of a random account from game_data.py.

    :returns: random account from game_data.py.

    """
    return random.choice(data)



def format_data(input_data):
    """
    Formats the data from account into a readable structure that can be compared.

    :returns: formatted string of account data.

    """
    return f"{input_data['name']} is a {input_data['description']} from {input_data['country']}."


def comparison(account_1=0, account_2=0):
    """
    Compares two dictionary values representing followers on instagram.

    Parameters:
    ----------
    :param account_1 (dict):  (Default value = 0)
        First account to be compared.

    :param account_2 (dict):  (Default value = 0)
        FirsSecondt account to be compared against the first.

    Returns:
    -------
    :returns bool: Whether value of the corresponding follower
        key of the first account is greater than second account.
        Or whether the data passed are dictionaries.
    """

    if isinstance(account_1, dict) and isinstance(account_2, dict):
        return account_1['follower_count'] >= account_2['follower_count']
    return False



def get_user_guess(account_1, account_2):
    """
    Gets the user input as to which account they think has more followers.
    It is passed the two accounts from which the name and description is
    presented to the user.
    From here the user is asked to choose one.
    Based on which account they've chosen, that is the first account to
    be compared against the other. I've done this to simplify the process.
    The account_1 parameter for the comparison function will be used to be
    represent either the first account of the game, or user inputs.

    The function then returns a bool value of the user inputted comparison,
    or failing that restarts the process.


    Parameters:
    ----------
    :param account_1 (dict):  (Default value = 0)
        First account to be compared.

    :param account_2 (dict):  (Default value = 0)
        FirsSecondt account to be compared against the first.

    Returns:
    -------
    :returns bool: Whether value of the corresponding follower
        key of the first account is greater than second account.
        Or whether the data passed are dictionaries.
    """


    if isinstance(account_1, dict) and isinstance(account_2, dict):
        print(f'{logo}\n\n\nCompare A:\t{format_data(account_1)} {vs}'
            + f'\nAgainst B:\t{format_data(account_2)}')
        user_guess = input('\nA or B?')

        if user_guess.upper() == 'A':
            print(f"You've chosen {account_1['name']}")
            return comparison(account_1, account_2)

        if user_guess.upper() == 'B':
            print(f"You've chosen {account_2['name']}")
            return comparison(account_2, account_1)

        print('Incorrect choice\nTry again:')
        get_user_guess(account_1, account_2)
    return False

# Check if user is correct.

def main_loop():
    score = 0
    account_1 = generate_random_account()
    account_2 = generate_random_account()

    while get_user_guess(account_1, account_2):
        print(f"{comparison(account_1, account_2)}, "
        + f"{account_1['follower_count']} {account_2['follower_count']}")
        score += 1
        account_1 = account_2
        account_2 = generate_random_account()
        print('Score: ', score, '\n',format_data(account_1), format_data(account_2))
        clear()

    print(f"{comparison(account_1, account_2)} == {account_1['name'],account_1['follower_count']}, "
        + f"{account_2['name'],account_2['follower_count']}\nScore was: {score}")

    replay = input('Play again? any character except N')

    if replay.upper() != 'N':
        clear()
        main_loop()
    else:
        clear()
        sys.exit()

if __name__ == "__main__":
    main_loop()
