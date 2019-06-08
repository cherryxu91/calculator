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
