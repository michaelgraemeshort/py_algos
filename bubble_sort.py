# bubble sort attempt

# first iteration moves biggest element to end of list
# next moves second biggest to second last position
# because it moves the biggest number of each pair endward

l = [3, 2, 5, 7, 6, 4, 4, 12, 555]

# def bubble_sort(l): 
#     while True:
#         swapping = False
#         for i in range(len(l) - 1):
#             pair = l[i:i + 2]
#             if pair[0] > pair[1]:
#                 l[i], l[i + 1] = pair[1], pair[0]
#                 swapping = True
#         if swapping == False:
#             break
#     # return l

# # print(bubble_sort(l))

# print(l)
# bubble_sort(l)
# print(l)

# seems to work. remember, not strictly necessary to return l

def bubble_sort(l):
    swapping = True
    while swapping:
        swapping = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapping = True
    return l

print(bubble_sort(l))

# from the course. much better