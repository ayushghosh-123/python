# with open("myfile.txt", "w") as file:
#     file.write("Hello, this is my first file.\n")
#     file.write("Python makes file handling easy.\n")
#     file.write("Learning how to handle files in python.\n")
# print("File written successfully.")

# with open("myfile.txt", "r") as file:
#     data = file.read()
#     print("File content:\n", data)

# with open("myfile.txt", "a") as file:
#     file.write("Appending a new line to the file.\n")
#     file.write("File handling is an essential skill.\n")
# print("Data appended successfully.")

# with open("myfile.txt", "r") as src, open("copyfile.txt", "w") as dest:
#     for line in src:
#         dest.write(line)
# print("Content copied successfully.")

# with open("myfile.txt", "r") as file:
#     print("Reading file line by line:")
#     for line in file:
#         print(line.strip())


# upper = lower = 0
# with open("myfile.txt", "r") as file:
#     for line in file:
#         print(line.strip())
#         for char in line:
#             if char.isupper():
#                 upper += 1
#             elif char.islower():
#                 lower += 1
# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)


vowels = "aeiouAEIOU"
with open("myfile.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            count = sum(1 for ch in word if ch in vowels)
            print(f"'{word}' -> {count} vowel(s)") 