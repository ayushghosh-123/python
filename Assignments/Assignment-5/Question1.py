def merge_list(list1, list2):
    return list1 + list2

list1 = list(map(int, input("Enter the element of first list: ").split()))
list2 = list(map(int, input("Enter the element of second list: ").split()))

list3 = merge_list(list1, list2)

print("merge list is: ", list3)
