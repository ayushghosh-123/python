def is_palindrome(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

value = input("Enter a string: ")
is_palindrome(value)
