def merge(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

l1 = input("Enter the first sorted list (space-separated): ")
l2 = input("Enter the second sorted list (space-separated): ")
list1 = [int(num) for num in l1.split()]
list2 = [int(num) for num in l2.split()]
merged_list = merge(list1, list2)
print("Merged List:", merged_list)
