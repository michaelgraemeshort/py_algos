import sort_algos
from random import randint
from timeit import timeit

list_size = int(input("Set list size: "))
max_integer_size = int(input("Set maximum integer size: "))
runs = int(input("Set number of runs: "))

algos = [
    sort_algos.bubble_sort,
    sort_algos.selection_sort,
    sort_algos.insertion_sort,
    sort_algos.merge_sort,
    sort_algos.quicksort,
    sorted
    ]

for run in range(1, runs + 1):
    test_list = [randint(0, max_integer_size) for i in range(list_size)]
    print(f"Run {run}:")
    for algo in algos:
        runtime = timeit("algo(test_list[:])", number=1, globals=globals())
        print(algo.__name__, ":", round(runtime, 5))
    print("------------------------")
