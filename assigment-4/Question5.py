def is_prime(num):
    if num < 2 : 
        return False
    for i in range (2, int(num **0.5)+1):
        if num % i == 0:
            return False
    return True

prime = [num for num in range (15, 26) if is_prime(num)]
print("prime number between 15 to 25 is: ", prime)