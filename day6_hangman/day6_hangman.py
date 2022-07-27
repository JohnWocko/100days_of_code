import random

try:
    with open('day6_hangman\words.txt', 'r') as file:
        words = file.read().split('\n')
except:
    words = ['hello', 'Killero']

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def get_word():
    word = random.choice(words)
    if word != ' ':
        return word.lower()
    else:
        get_word()


def display(word, guessed=[], guesses=0):
    count = 0
    print(HANGMANPICS[guesses])
    for letter in word:
        if letter not in guessed:
            print(' - ', end='')
        else:
            print(f' {letter} ', end='')
            count += 1
    print('\n')
    if count >= 6:
        print('All letters guessed')
        return True


def get_user_guess():
    try:
        user_guess = input('\nPlease enter a single character:')
        if len(user_guess) > 1:
            print('More than one character inputted, first one taken as guess')
            return user_guess[0].lower()
        else:
            print(f'Guess is : {user_guess}')
            return user_guess.lower()
    except:
        print('Input error, try again')
        get_user_guess()


def check_letter(letter, word):

    print(f'{letter} is Right' if letter in word else f'{letter} is Wrong')
    return (letter in word)


def main_loop():
    guessed_correctly = []
    guessed_incorrectly = []
    won = False
    chosen_word = get_word()
    guesses = 0

    while not won or guesses <= 6:
        won = display(chosen_word, guessed_correctly, guesses)
        #print(f'Total incorrect guesses: {guesses}\tCorrect letters guessed: {guessed_correctly}\tIncorrect Guesses: {guessed_incorrectly}')
            
        if won:
            print('Well done!')
            break

        else:
            user_guess = get_user_guess()
            if check_letter(user_guess, chosen_word) and user_guess not in guessed_correctly:
                guessed_correctly.extend(user_guess)
            elif user_guess not in guessed_incorrectly and user_guess not in guessed_correctly:
                guessed_incorrectly.extend(user_guess)
                guesses += 1
            else:
                print('You\'ve already inputted this guess.')

        if guesses >= 6:
            print(
                f'\n---------------- GAME OVER ----------------\nSorry, word was {chosen_word}')
            display(chosen_word, guessed_correctly, guesses)
            break
        print(f'Total incorrect guesses: {guesses}\tCorrect letters guessed: {guessed_correctly}\tIncorrect Guesses: {guessed_incorrectly}')
        


if __name__ == '__main__':
    main_loop()
