import random

def main():
    difficulty_settings = {'E':10, 'M': 7, 'H': 5}
    random_num = random.randint(1,200)
    
    try:
        user_dif = input('Play the game in Easy, Medium or Hard? E/M/H')
        difficulty = difficulty_settings[user_dif.upper()]
        user_input = -1
        tries = 0
        print(difficulty)
        while user_input != random_num and tries <= difficulty:
            user_input = int(input('Please enter your guess:\n'))
            print(tries, difficulty)
            if user_input > random_num:
                print('Incorrect! - Too high')
                tries+=1
                continue
            elif user_input < random_num:
                print('Incorrect! - Too low')
                tries+=1
                continue

        if tries>= difficulty:
            print(f'You Lost, number was {random_num}')
        else:
            print('Guess was correct')
    except:
        print('You\'ve entered an invalid input.')
        main()

if __name__ == '__main__':
    main()