num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]

print("Difference:", max(digits) - min(digits))
