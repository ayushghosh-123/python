n = int(input("Enter the value of n: "))
odd_numbers = [i for i in range(2*n - 1, 0, -2)]
print(f"First {n} odd numbers in descending order: {odd_numbers}")
