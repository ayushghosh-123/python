num = input("enter the integer number: ")
digits = list(map(int, num))

sum_of_digits = sum(digits)
largest_digits = max(digits)
smallest_digit = min(digits)
digit_count = len(digits)
difference = largest_digits - smallest_digit

frequency = {digit: digits.count(digit) for digit in digits }

print(f"sum of digits: {sum_of_digits}")
print(f"largest  digits: {largest_digits}")
print(f"number of digits: {digit_count}")
print(f"difference between largest and smallest : {difference}")
print(f"Frequency of each digit: {frequency}")