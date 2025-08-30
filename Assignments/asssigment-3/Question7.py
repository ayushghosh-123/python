user_input = input("Enter a sentence: ")
words = user_input.split()
long_word = " "
max_length = 0

for i in words: 
    if len(i) > max_length:
        longest_word = i
        max_length = len(i)
        
print("longest word is: ", longest_word)
print("maximum length is: ", max_length) 