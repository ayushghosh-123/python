def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get the weight in kilograms from the user
weight = float(input("Enter your weight in kilograms: "))

# Get the height in meters from the user
height = float(input("Enter your height in meters: "))

# Calculate the BMI
bmi = calculate_bmi(weight, height)

print(f"Your BMI is {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")