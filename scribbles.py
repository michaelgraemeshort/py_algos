# recursion practice

# reverse a string recursively

# start at the end
# no loops!
# just has to take the last letter of the string, or a slice of the string

# I want "wah" in, and "haw" out

# should basically look like

def reverse_string(string):
    if len(string) < 2:
        return string
    else:
        return string[-1] + reverse_string(string[:-1])

# I want it to work like this

# fn("wah") returns "h" + fn("wa")
# fn("wa") returns "a" + fn("w")
# fn("w") returns "w"

# string has to diminish in size with every call

# print(reverse_string("bugger"))

#---#

# print all of the elements in a list, no loops


test_list = [1, 2, 3, 4, 5]


def print_elements(l):
    if not l:
        return
    else:
        print(l[0])
        print_elements(l[1:])

# print_elements(test_list)

#---#

# try implementing a map function, no loops

def tst_fn(n):
    return n * 2

def recursive_map(fn, l):
    if len(l) < 2:
        return [fn(l[0])]
    else:
        return [fn(l[0])] + recursive_map(tst_fn, l[1:])

# again, I want this to stop when it reaches the end of the iterable

print(recursive_map(tst_fn, test_list))

# works but a minute later I have forgotten why
# ok imagine a 2 length list
# would return both (transformed) elements
# if there are more elements, it just goes to the base case, then back-propagates to the beginning
