# For this day, a tip calculator was built.

def tip_calculator():
    try:
        percent = float(input('Welcome to the tip calculator:\nPlease enter percentage:\n'))
        total = float(input('Please enter total:\n'))
        people = int(input('Please enter how many people:\n'))

        if type(percent) and type(total) is float or int:
            tip = total*(percent/100)
            final_total = tip + total
            divided_total = final_total / people
            print(f'{percent:.2f}% of £{total:.2f} == £{tip:.2f}\nTotal including tip is £{final_total:.2f}\nDivided up for {people} individuals, total is £{divided_total:.2f} per person')
    except:
        print('Input given not correct type')
        tip_calculator()

if __name__ == '__main__':
    tip_calculator()
    