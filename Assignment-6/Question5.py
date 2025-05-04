text = input("enter any string: ")

upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())\
    
print("uppercase letter: ", upper)
print("lowercase letter: ", lower)