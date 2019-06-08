x = float(input('What is the first number?\n'))
operator = input('What do you want to do with number?\n')
y = float(input('What is the second number?\n'))

if operator == '+' :
    print(x + y)
elif operator == '-' :
    print(x - y)
elif operator == '/' :
    print(x / y)
elif operator == '*' :
    print(x * y)
else:
    print('Invalid operator. Please try again.')

# to do
# use 'try/except' for each variable to make sure it's a number and not a string
# include 'input' for 'else:' to reprompt Calculator
# make a loop for 'else'
