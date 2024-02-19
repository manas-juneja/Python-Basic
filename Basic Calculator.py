First_Number = float(input("Enter First Number: "))
Operator = input("Choose your operation: +, -, *, /, %: ")
Second_Number = float(input("Enter Second Number: "))

if Operator == '+':
    print(First_Number + Second_Number)
elif Operator == '-':
    print(First_Number - Second_Number)
elif Operator == '/':
    print(First_Number / Second_Number)
elif Operator == '*':
    print(First_Number * Second_Number)
elif Operator == '%':
    print(First_Number % Second_Number)
else:
    print("Invalid operation")