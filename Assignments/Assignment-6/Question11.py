import random
import statistics

nums = list(range(10, 100, 3))
random_nums = random.sample(nums, 6)

print("Numbers: ", random_nums)
print("Mean: ", statistics.mean(random_nums))
print("Median: ", statistics.median(random_nums))
print("Mode: ", statistics.mode(random_nums))
