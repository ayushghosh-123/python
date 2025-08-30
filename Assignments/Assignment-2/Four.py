def create_number(n):
    num1 = n
    num2 = n + 1
    num3 = n + 2
    return f"{num1}{num2}{num3}"

# Get the single digit from the user
n = int(input("Enter a single digit (1-7): "))

# Ensure the input is within the range
if 1 <= n <= 7:
    result = create_number(n)
    print(f"The 3-digit number is: {result}")
else:
    print("Please enter a valid single digit in the range 1-7.")
