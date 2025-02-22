# Define constants
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24

# Get user input
year = int(input("Enter the year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_per_year = 366  # Leap year
else:
    days_per_year = 365  # Non-leap year

# Calculate total seconds in the year
seconds_in_a_year = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year

# Print the result
print(f"The number of seconds in the year {year} is: {seconds_in_a_year}")



