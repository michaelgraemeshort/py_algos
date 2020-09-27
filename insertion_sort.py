# start at index 1
# check if element at index 0 is bigger
# swap if so
# move to index 2
# check if element at index 1 is bigger
# swap if so, THEN check if element at index 0 is bigger, and swap if so
# basically, compare each element to the one to its left, swap as many times as necessary until the integer to its left is smaller

from random import shuffle

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
shuffle(test_list)

def insertion_sort(l):
    if l:
        for i in range(1, len(l)):
            x = i                                       # x keeps track of which indices are being compared
            for j in range(i):                          # j runs a maximum of i times to swap an element all the way to 0 if necessary
                if l[x] < l[x - 1]:
                    l[x], l[x - 1] = l[x - 1], l[x]
                    x -= 1
                else:
                    break                               # stops j wastefully running more often than necessary
    return l

print(test_list)
print(insertion_sort(test_list))