text = input("Enter the string: ")
upper_count = sum(1 for char in text if char.isupper())
lower_count = sum(1 for char in text if char.islower())

print(f"uppercase letter: {upper_count}")
print(f"lowercase letter: {lower_count}")