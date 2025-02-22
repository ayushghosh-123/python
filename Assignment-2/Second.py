def average_temperature(temperatures):
    total_temperature = sum(temperatures)
    average = total_temperature / len(temperatures)
    return average

# Get the temperatures for each day from the user
temperatures = []
for i in range(7):
    temp = float(input(f"Enter the temperature for day {i+1}: "))
    temperatures.append(temp)

# Calculate the average temperature
average_temp = average_temperature(temperatures)

print(f"The average temperature for the week is {average_temp:.2f}°C")
