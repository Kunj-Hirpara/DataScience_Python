def remove_duplicates(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
    return new_list

list1 = [10, 20, 10, 30, 20, 40, 50, 30]
print("Original List: ", list1)

list2 = remove_duplicates(list1)
print("List After Removing Duplicates: ", list2)