# insertion sort

from random import randint

l = [randint(0, 9) for i in range(10)]
t = [3, 2, 1]

# take each element after the first and move as far to the left as necessary by swapping with its left adjacent


def insertion_sort(l):
    for i in range(1, len(l)):
        x = i
        for j in range(i):
            if l[x] < l[x - 1]:
                l[x], l[x - 1] = l[x - 1], l[x]
                x -= 1
            else:
                break


print(l)
insertion_sort(l)
print(l)