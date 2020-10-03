# generate list of random integers
# list size and range of integers to be specified by user at runtime

import functions
from timeit import timeit

list_size = int(input("Set list size: "))
max_integer_size = int(input("Set maximum integer size: "))
runs = int(input("Set number of runs: "))
fns = [
    functions.bubble_sort,
    functions.selection_sort,
    functions.insertion_sort,
    functions.merge_sort,
    functions.quicksort
    ]

for run in range(1, runs + 1):
    test_tuple = tuple(functions.create_test_list(list_size, max_integer_size))
    for fn in fns:
        runtime = timeit(f"{fn(list(test_tuple))}", number=1, globals=globals())
        print(fn.__name__, round(runtime, 5))
    builtin_time = timeit(f"{list(test_tuple)}.sort()", number=1, globals=globals())
    print("built-in", round(builtin_time, 5))
    print("-----------------------")
