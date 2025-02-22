def reverse_number(number):
    reversed_num = str(number)[::-1]
    return int(reversed_num)

# Get the 3-digit number from the user
number = int(input("Enter a 3-digit number: "))

# Ensure the input is a 3-digit number
if 100 <= number <= 999:
    result = reverse_number(number)
    print(f"The reversed number is: {result}")
else:
    print("Please enter a valid 3-digit number.")
