# do recursive stuff on paper if confused
# the order of execution is the confusing part
# wherever the function is called, you have to follow it down the rabbit hole until the base condition is met, then back up again
# paper!

from random import shuffle

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
shuffle(test_list)


def merge(list_1, list_2):
    sorted_list = []
    while list_1 and list_2:
        if list_1[0] > list_2[0]:
            sorted_list.append(list_2.pop(0))
        else:
            sorted_list.append(list_1.pop(0))
    while list_1:
        sorted_list.append(list_1.pop(0))
    while list_2:
        sorted_list.append(list_2.pop(0))
    return sorted_list


def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        middle = len(l) // 2
        left = merge_sort(l[:middle])
        right = merge_sort(l[middle:])
        return merge(left, right)

print(merge_sort(test_list))


# def merge_sorted_lists(list_1, list_2):
#     merged_list = []
#     i = j = 0
#     while i < len(list_1) and j < len(list_2):  # runs until one list is exhausted
#         if list_1[0] > list_2[0]:
#             merged_list.append(list_2[j])
#             j += 1
#         else:
#             merged_list.append(list_1[i])
#             i += 1
#     # while i < len(list_1):
#     #     merged_list.append(list_1[i])
#     #     i += 1
#     # while j < len(list_2):
#     #     merged_list.append(list_2[j])
#     #     j += 1
#     if list_1:  # mopping up remaining elements
#         merged_list.extend(list_1[i:])
#     if list_2:
#         merged_list.extend(list_2[j:])
#     return merged_list


# def merge_sort(l):
#     if len(l) < 2:
#         return l[:]
#     else:
#         middle = len(l) // 2
#         list_1 = merge_sort(l[:middle])
#         list_2 = merge_sort(l[middle:])
#         return merge_sorted_lists(list_1, list_2)


# list_1 = [1, 3, 5, 7]
# list_2 = [2, 4, 6, 8, 10]
# print(merge(list_1, list_2))

# print(merge_sort(test_list))

# this is broken as fuck
# come back to it and redo from scratch because makes zero fucking sense
# change something, undo change, continue to get changed outcome
# what the fucking fuck
# glitch in the fucking matrix or
