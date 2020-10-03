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
        runtime = timeit(f"fn(list(test_tuple))", number=1, globals=globals())
        print(fn.__name__, "->", round(runtime, 5))
    builtin_time = timeit(f"{list(test_tuple)}.sort()", number=1, globals=globals())
    print("built-in", "->", round(builtin_time, 5))
    print("------------------------")


# # generate list of random integers
# # list size and range of integers to be specified by user at runtime

# import functions
# import timeit

# list_size = int(input("Set list size: "))
# max_integer_size = int(input("Set maximum integer size: "))
# runs = int(input("Set number of runs: "))

# for run in range(1, runs + 1):
#     test_tuple = tuple(functions.create_test_list(list_size, max_integer_size))
#     test_list = list(test_tuple)
#     bubble_time = timeit.timeit(
#         "functions.bubble_sort(test_list)", number=1, globals=globals())
#     test_list = list(test_tuple)
#     selection_time = timeit.timeit(
#         "functions.selection_sort(test_list)", number=1, globals=globals())
#     test_list = list(test_tuple)
#     insertion_time = timeit.timeit(
#         "functions.insertion_sort(test_list)", number=1, globals=globals())
#     test_list = list(test_tuple)
#     merge_time = timeit.timeit(
#         "functions.merge_sort(test_list)", number=1, globals=globals())
#     test_list = list(test_tuple)
#     quick_time = timeit.timeit(
#         "functions.quicksort(test_list)", number=1, globals=globals())
#     test_list = list(test_tuple)
#     builtin_time = timeit.timeit(
#         "test_list.sort()", number=1, globals=globals())
#     print(f"Run {run}:")
#     print(f"Bubble Sort: {round(bubble_time, 5)}")
#     print(f"Selection Sort: {round(selection_time, 5)}")
#     print(f"Insertion Sort: {round(insertion_time, 5)}")
#     print(f"Merge Sort: {round(merge_time, 5)}")
#     print(f"Quicksort: {round(quick_time, 5)}")
#     print(f"Built-In Sort: {round(builtin_time, 5)}")
#     print("-----------------------")
