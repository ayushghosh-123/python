def print_pattern(word):
    n = len(word)
    
    for i in range(n):
        # Repeat the character (i+1) times and center it with spacing
        print(" ".join([word[i]] * (i + 1)).rjust(n * 2))

print_pattern("python")
