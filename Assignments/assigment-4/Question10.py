List1 = [10, 20, 30, 40, 50, 60]
search_num = int(input("Enter a number to search: "))
count = List1.count(search_num)

if count > 0:
    print(f"{search_num} is present in the list {count} time(s).")
else:
    print(f"{search_num} is not present in the list.")
 
