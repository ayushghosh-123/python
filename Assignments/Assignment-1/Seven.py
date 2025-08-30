def cm_to_feet_inches(cm):
    total_inches = cm / 2.54
    feet = int(total_inches // 12)
    inches = total_inches % 12
    return feet, inches

# Get the height in centimeters from the user
cm = float(input("Enter your height in centimeters: "))

# Convert to feet and inches
feet, inches = cm_to_feet_inches(cm)

print(f"Your height is {feet} feet and {inches:.2f} inches.")
