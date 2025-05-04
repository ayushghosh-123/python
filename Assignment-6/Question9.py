list_one = list(map(int, input("enter the list: ").split()))

lst = [x*2 for x in list_one]
lst = [x+1 for x in list_one]

print("Ascending: ", sorted(lst))
print("Descending", sorted(lst, reverse = True))