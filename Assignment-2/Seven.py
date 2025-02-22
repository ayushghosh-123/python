import cmath

def calculate_roots(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    # Calculate two solutions
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    
    return root1, root2

# Get coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the roots
root1, root2 = calculate_roots(a, b, c)

print(f"The roots of the quadratic equation are {root1} and {root2}")
