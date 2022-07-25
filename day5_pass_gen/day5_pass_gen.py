import string
import random


def password_generator():
    try:
        length = int(input('Enter a password length:\n'))
        chars = string.ascii_letters + string.digits + '!#!"£$%^&*()_+\{\}[]\';:<>/\/?|,.'
        random_password = ''.join(random.sample(chars, length))
        return random_password
    except:
        print('Please input an integer whole number')
        password_generator()
    

if __name__ == '__main__':

    password = password_generator()
    print(f'Your password is {password}')