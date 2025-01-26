# coding: utf-8
# attempt to convert and divide values using simple exception handling
while True:
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    except ValueError:
        print('You must enter two integers\n')
    except ZeroDivisionError:
        print('Attempted to divide by zero\n')
    # executes only if no exceptions occur
    else:
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break
        
