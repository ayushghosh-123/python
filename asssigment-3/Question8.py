user_input = input("enter the sentence in lowercase: ")
vowel = 'aeiou'
words = user_input.split()

for word in words:
    count = sum(1 for char in word if char in vowel)
    print(f"{word.capitalize(): <15} {count}")