import math

# Function to calculate the polynomial
def calculate_polynomial(x, y, z):
    result = 4 * (x ** 4) + 3 * (y ** 3) + 9 * (z ** 2) + 6 * math.pi
    return result

# Taking input from the user
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))

# Calculating the result
result = calculate_polynomial(x, y, z)

# Displaying the result
print(f"The result of the polynomial 4x^4 + 3y^3 + 9z^2 + 6π is: {result}")
