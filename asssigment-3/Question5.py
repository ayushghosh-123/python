user_input = input("enter your input value: ")

word = user_input.split()
reverse_sentence = ' '.join(reversed(word))

print("reverse sentence is :", reverse_sentence)