import random

try:
    with open('day6_hangman\words.txt', 'r') as file:
        words = file.read().split('\n')
except:
    words = ['hello','Killero']


def get_word():
    word = random.choice(words)
    if word != ' ': 
        return word.lower()
    else:
        get_word()

def display(word, guessed = []):
    count = 0
    for letter in word:
        if letter not in guessed:
            print(' - ', end = '')
        else:
            print(f' {letter} ', end = '')
            count+=1
    print('\n')
    if count == len(word):
        print('All letters guessed')
        return True
    else:
        return False

def get_user_guess():
    try:
        user_guess = input('Please enter a single character:')
        if len(user_guess) > 1:
            print('More than one character inputted, try again')
            get_user_guess()
        else:
            print(f'Guess is : {user_guess}')
            return user_guess.lower()
    except:
        print('Input error, try again')
        get_user_guess()

def check_letter(letter, word):
    print('Right' if letter in word else 'Wrong')
    return (letter in word)

def main_loop():
    guessed = []
    won = False
    chosen_word = get_word()
    guesses = len(chosen_word)

    while not won and guesses > 0:
        print(guesses)
        won = display(chosen_word, guessed)
        user_guess = get_user_guess()
        if check_letter(user_guess, chosen_word):
            guessed.extend(user_guess)
        else:
            guesses -=1
    
    if won:
        print('Well done!')
    else:
        print(f'Sorry, word was {chosen_word}')



if __name__ == '__main__':
    main_loop()

