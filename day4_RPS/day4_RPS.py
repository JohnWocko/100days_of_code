import random


def rps():
    
    selection = 'RPS'
    rules = {'R': ['S', 'Rock'], 'P': ['R', 'Paper'], 'S':['P', 'Scissors']}
    comp_choice = random.choice(selection)

    usr_choice = input('What do you choose? Rock - R, Paper - P or Scissors - S:')

    if usr_choice.upper() == comp_choice:
        print(f'You both chose {usr_choice}')
        rps()
        return True
    else:
        if usr_choice.upper() in rules:
            if rules[usr_choice.upper()][0] == comp_choice:
                print(f'You Won! you chose {rules[usr_choice.upper()][1]} which beats {rules[comp_choice][1]}')
            elif rules[comp_choice][0] == usr_choice.upper():
                print(f'You lost! Computer chose {rules[comp_choice][1]} which beats your {rules[usr_choice.upper()][1]}')
    
    play_again = input('Play again? Yes - Y')
    if play_again.upper() == 'Y':
        rps()
    else:
        exit()
rps()