def is_palidrome(s):
    return s == s[::-1]

word = input("enter your input: ")
print(is_palidrome(word))
