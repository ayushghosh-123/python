def is_palindrom(string):
    cleaned = string.replace(" ", "").lower()
    if cleaned == cleaned[::-1]: 
        print("the string is a palindrom")
    else:
        print("the string is not palindrom")
        
value = input("enter the string: ")
is_palindrom(value)