# start and end indices are used to calculate the middle index
# and optionally, in this case, the start and end points of the search, much like Python's builtin index method
# if you have determined that x is less than the middle index value, you should consider the list UP TO that value
# if more, consider the list FROM the value AFTER
# doesn't matter if the middle of [0, 1] is 0 or 1
# the hard part: off-by-one errors. check edge cases (first/last elements)
# base case: should return -1 if lst is empty

def binary_search(lst, x, start=None, end=None):
    if start == None and end == None:
        start = 0
        end = len(lst) # 2
    if start == end:
        return -1
    middle = (start + end) // 2 # 1
    if lst[middle] == x:
        return middle
    if lst[middle] > x:
        return binary_search(lst, x, start, middle) # [0, 1], 0, 0, 1
    return binary_search(lst, x, middle + 1, end)


test_list = range(4)
# for i in range(-1, 5):
#     print(binary_search(test_list, i))

# print(binary_search(test_list, 2, 2, 4))

# print(test_list.index(2, 2, 4))  # this doesn't work in VSCode but does in Ubuntu Python interface(??)

# now do iterative version

def binary_search_2(l, n):
	start = 0
	end = len(l)
	while start < end:
		middle = (start + end) // 2
		if l[middle] == n:
			return middle
		if l[middle] < n:
			start = middle + 1
		else:
			end = middle
	return -1