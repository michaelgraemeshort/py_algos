# recursively split list down to its individual elements
# rebuild list in sorted order by:
# when merging two single elements, obviously put the smaller element on the left
# when one or both of the lists to be merged contains multiple elements, you can do this:
# compare the first element of the first list to the first element of the second
# add the smaller to a new list
# compare the other element to the second element of the list that had the smaller element
# add the smaller to the new list
# etc. basically just taking the smallest element, whichever list it belongs to, until they are all in the new list
# you can do this because the sublists are sorted

from random import shuffle

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
shuffle(test_list)

def merge_sorted_lists(list_1, list_2):
    merged_list = []
    i = j = 0
    while i < len(list_1) and j < len(list_2):  # runs until one list is exhausted
        if list_1[0] > list_2[0]:
            merged_list.append(list_2[j])
            j += 1
        else:
            merged_list.append(list_1[i])
            i += 1
    if list_1:  # mopping up remaining elements
        merged_list.extend(list_1[i:])
    if list_2:
        merged_list.extend(list_2[j:])
    return merged_list

list_1 = [1, 3, 5, 7]
list_2 = [2, 4, 6, 8, 10]
print(merge_sorted_lists(list_1, list_2))