a = float(input("enter the first number: "))
b = float(input("enter the second number: "))

operator = input("enter the operator (+, -, *, /): ")

if operator == '+':
    print("result: ", a+b)
elif operator == '-':
    print("result: ", a-b)
elif operator == '*':
    print("result: ", a*b)
elif operator == '/':
    if b != 0:
        print("Result: ",a/b)
    else:
        print("cannot divided by zero ")
else:
    print("Invalid operator ")