while True:
    number1 = input('Please enter a number.\n')

    try:
        number1 = float(number1)
        break

    except:
        pass

while True:
    operator = input('What do you want to do with number?\n')
    try:
        if operator == '+' :
            print(number1 + number2)
        elif operator == '-' :
            print(number1 - number2)
        elif operator == '/' :
            print(number1 / number2)
        elif operator == '*' :
            print(number1 * number2)
        break

    except:
        print('Invalid operator. Please try again.')
        pass

# while True:
#     operator = input('What do you want to do with number?\n')
#
#     try:
#         operator = '+, -, /, *, or ^'
#         if operator == '+' :
#             print(x + y)
#         elif operator == '-' :
#             print(x - y)
#         elif operator == '/' :
#             print(x / y)
#         elif operator == '*' :
#             print(x * y)
#         elif operator == '^' :
#             print(x ** y)
#         break
#
#     except:
#         print('Invalid operator. Please try again.')
#         pass

# number2 = input('What is the second number?\n')
#
while True:
    number2 = input('Please enter a number.\n')

    try:
        number2 = float(number2)
        break

    except:
        pass
# above is y = float(input('What is the second number?\n'))

# to do
# use 'try/except' for each variable to make sure it's a number and not a string
# include 'input' for 'else:' to reprompt Calculator
# make a loop for 'else'
