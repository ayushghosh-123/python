employee = {}

while True:
    name = input("enter the employee name: ")
    salary = input("enter the salary: ")
    employee[name] = salary
    
    count = input("Add another? (yes/no): ")
    if count.lower() != 'yes':
        break
    
print(employee)