def sum_even():
    return sum(i for i in range(100, 501) if i%2 == 0)

print("Sum: ", sum_even())