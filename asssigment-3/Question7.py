user_input = input("Enter a sentence: ")
words = user_input.split()
long_word = " "
max_length = 0

for word in words: 
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)
        
print("longest word is: ", longest_word)
print("maximum length is: ", max_length) 