# make an input for 1st number
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

# add = (float(number1) + float(number2))
# subtract = (float(number1) - float(number2))
# divide = (float(number1) / float(number2))
# multiply = (float(number1) * float(number2))

# make a function to call operator after entering num1, num2, and operator
def operation(num1, operator, num2):
    operator == '+', '-', '/', '*'
# set operators as variables in function
    add = num1 + num2
    subtract = num1 - num2
    divide = num1 / num2
    multiply = num1 * num2
    if  operator == '+' :
        print(num1, '+', num2, '= ', add)
    elif operator == '-' :
        print(num1, '-', num2, '= ', subtract)
    elif operator == '/' :
        print(num1, '/', num2, '= ', divide)
    elif operator == '*' :
        print(num1, '*', num2, '= ', multiply)

operation(num1, operator, num2)
print(num1)
print(operator)
print(num2)
# to do
# use 'try/except' for each variable to make sure it's a number and not a string
# make a loop for operator and use 'try/except' too
