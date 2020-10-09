'''
1) write function to create a list of x fake email addresses
2) append my email to the list
3) sort the list (use builtin)
4) search the list for my email
5) print time taken by creation and search functions
'''

import random
import string
import time


def execution_timer(fn):
    def inner(*args, **kwargs):
        start = time.time()
        fn_output = fn(*args, **kwargs)
        stop = time.time()
        runtime = stop - start
        return fn_output, runtime
    return inner


@execution_timer
def make_fake_email_addresses(n):
    local_part_characters = (string.ascii_letters +
                             string.digits + "!#$%&'*+-/=?^_`{|}~.") * 3
    domains = "@example.com", "@spam.com", "@eggs.com"
    addresses = []
    while len(addresses) < n:
        local_part = random.sample(local_part_characters, 10)
        if local_part[0] != "." and local_part[-1] != ".":
            local_part = "".join(local_part)
            addresses.append(local_part + random.choice(domains))
    return addresses


@execution_timer
def search_email_addresses(addresses, target):
    start = 0
    end = len(addresses)
    while start < end:
        middle = (start + end) // 2
        if addresses[middle] == target:
            return middle
        if addresses[middle] < target:
            start = middle + 1
        else:
            end = middle
    return -1


num_fakes = 100000
print("Creating list of fake email addresses...")
test_list, time_1 = make_fake_email_addresses(num_fakes)
print(f"{num_fakes} addresses created in {round(time_1, 5)} seconds.")
test_email = "michael.g.short@hotmail.co.uk"
print(f"Adding test email address {test_email} to list of addresses.")
test_list.append(test_email)
print("Sorting list...")
test_list = sorted(test_list)
print("Searching list...")
search_result, time_2 = search_email_addresses(test_list, test_email)
print(f"{test_email} found in list at index {search_result}. Search time {round(time_2, 5)} seconds.")
