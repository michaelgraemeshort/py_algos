# selection sort attempt

# starts at index 0
# compares element at 0 with each other element
# if other element is smaller, swaps elements, thus placing smallest at beginning
# next iteration starts at index 1

from random import shuffle

l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
shuffle(l)

def selection_sort(l):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

print(l)
print(selection_sort(l))