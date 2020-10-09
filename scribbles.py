# def binary_search(my_list, number, start_index=None, end_index=None):
#     if start_index == None and end_index == None:
#         start_index = 0
#         end_index = len(my_list)
#     if start_index == end_index:
#         return -1
#     middle_index = (start_index + end_index) // 2
#     if my_list[middle_index] == number:
#         return middle_index
#     elif my_list[middle_index] < number:
#         start_index += (end_index - start_index + 1) // 2
#         return binary_search(my_list, number, start_index, end_index)
#     end_index -= (end_index - start_index + 1) // 2
#     return binary_search(my_list, number, start_index, end_index)


# for i in range(-4, 8):
#     print(binary_search([0, 1, 2, 3], i))

# this expression (end_index - start_index + 1) has + 1 in it to avoid RecursionError
# use of floor division means the + 1 has no effect until end_index - start_index == 1
# this is also not the most elegant implementation. try:

def binary_search(my_list, number, start_index=None, end_index=None):
    if start_index == None and end_index == None:
        start_index = 0
        end_index = len(my_list) - 1
    if end_index < start_index:  # should search a single item list! but not a zero item list
        return -1
    middle_index = (start_index + end_index) // 2
    if my_list[middle_index] == number:
        return middle_index
    elif my_list[middle_index] < number:
        return binary_search(my_list, number, middle_index + 1, end_index)
    return binary_search(my_list, number, start_index, middle_index - 1)


test_list = [0, 1, 2, 3]
for i in range(-1, 5):
    print(binary_search(test_list, i))
