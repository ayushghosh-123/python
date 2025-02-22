# Get input from the user
character = input("Enter a character: ")

# Ensure the input is a single character
if len(character) == 1:
    # Get the ASCII value using ord()
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is: {ascii_value}")
else:
    print("Please enter only a single character.")
