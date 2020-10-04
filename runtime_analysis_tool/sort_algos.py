from random import randint


def bubble_sort(l):
    swapping = True
    while swapping:
        swapping = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapping = True
    return l


def selection_sort(l):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


def insertion_sort(l):
    if l:
        for i in range(1, len(l)):
            x = i
            for j in range(i):
                if l[x] < l[x - 1]:
                    l[x], l[x - 1] = l[x - 1], l[x]
                    x -= 1
                else:
                    break
    return l


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


def quicksort(l):
    if len(l) < 2:
        return l
    else:
        less = quicksort([i for i in l if i < l[-1]])
        equal = [i for i in l if i == l[-1]]
        more = quicksort([i for i in l if i > l[-1]])
        return less + equal + more
