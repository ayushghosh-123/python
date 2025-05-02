marks = [int(input(f"Enter marks of subject {i+1}:")) for i in range (6)]
print("marks scored in each subject: ", marks)
print("Total marks: ", sum(marks))
print("Highest marks: ", max(marks))
print("Lowest marks: ", min(marks))