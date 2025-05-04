user_input = input("enter a sentence: ")
word = user_input.split()
first_letter = ' '.join(i[0] for i in word if word)
print("format the firstword: ", first_letter)