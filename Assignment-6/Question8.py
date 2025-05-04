employee = {"john": 900000, "Ravi": 1200000, "Anita": 150000, "karan": 8000}

count = sum (1 for salary in employee.values() if salary > 10000)

print("employee earning more than 1 lakh: ", count)