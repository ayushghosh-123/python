for num in range (15, 26):
    if num>1:
        for i in range (2, num):
            if num % 2 == 0:
                break
            else:
                print(num,"is prime")