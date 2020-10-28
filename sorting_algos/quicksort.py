from random import randint

test_list = [randint(-10, 10) for i in range(20)]


def quicksort(l):
    if len(l) < 2:
        return l
    else:
        less = quicksort([i for i in l if i < l[-1]])
        equal = [i for i in l if i == l[-1]]
        more = quicksort([i for i in l if i > l[-1]])
        return less + equal + more


print(quicksort(test_list))
