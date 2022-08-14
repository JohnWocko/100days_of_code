
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2    

def power_of(n1, n2):
    return n1 * n2

operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '\\': divide, 
    '^':power_of 
    }

def calculator():
    num1 = int(input('Please enter number 1:'))
    num2 = int(input('Please enter number 2:'))

    for symbol in operations:
        print(symbol)
    operation_symbol = input('Pick an operation from above:')
    calculation_function = operations[operation_symbol]
    print(f'{num1} {operation_symbol} {num2} = {calculation_function(num1,num2)}')


def main():
    should_continue = True
    while should_continue:
        calculator()
        user_input = input('Run again? Y/N')

        if user_input.lower() != 'n':
            continue
        else:
            should_continue = False


if __name__ == '__main__':
    main()