# do recursive stuff on paper if confused
# the order of execution is the confusing part
# wherever the function is called, you have to follow it down the rabbit hole until the base condition is met, then back up again
# paper!

from random import randint

test_list = [randint(-10, 10) for i in range(20)]


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
