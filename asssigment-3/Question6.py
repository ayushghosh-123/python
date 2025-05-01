user_input = input("enter a sentence: ")
word = user_input.split()
first_letter = ' '.join(word[0] for word in word if word)
print("format the firstword: ", first_letter)