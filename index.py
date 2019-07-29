# use 'try/except' for each variable to make sure it's a number and not a string

# make a loop so user inputs 1st number
while True:
    num1 = input('Please enter a number.\n')

    try:
        num1 = float(num1)
        break

    except:
        pass

# prompt user to input which operator to use
while True:
    operator = input('What do you want to do with number? Choose: +, -, /, *\n')
    if operator.lower() not in ('+', '-', '/', '*'):
        print('Please enter an operator.\n')
    else:
        break

# make a loop to prompt user to enter a number
while True:
    num2 = input('Please enter a number.\n')

    try:
        num2 = float(num2)
        break

    except:
        pass

# make a function to call operator after entering num1, num2, and operator
def operation(num1, operator, num2):
    if operator == '+' :
        return num1 + num2
    elif operator == '-' :
        return num1 - num2
    elif operator == '/' :
        return num1 / num2
    elif operator == '*' :
        return num1 * num2

result = operation(num1, operator, num2)
finalans = round(result, 2)
print(finalans)
