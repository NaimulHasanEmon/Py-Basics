number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
number1 = int(number1)
number2 = int(number2)
operation = input("Which operation to perform (+ or - or * or / or %): ")
if (operation == '+'):
    print(number1 + number2)
elif (operation == '-'):
    print(number1 - number2)
elif (operation == '*'):
    print(number1 * number2)
elif (operation == '/'):
    print(number1 / number2)
elif (operation == '%'):
    print(number1 % number2)
else:
    print("Invalid operation")
