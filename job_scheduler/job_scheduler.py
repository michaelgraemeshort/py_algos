# error handling woes
# end time must be after start time
# separate add-to-list and add-to-tree functions
# job should ONLY be added to list if successfully added to tree first
# tree.insert() should RETURN a value rather than simply printing success/not
# likewise remove from list/tree
# get_job should only return job if it is valid
# backup is job_scheduler2 so this is fair game for whatever

from classes2 import Node, BinarySearchTree
from csv import reader, writer
import re


def convert_time(time):
    """convert time from hh:dd to minutes after 00:00"""
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)


def valid_start_time(start_time):
    """ensures user-input start time is valid"""
    pattern = r"[0-2]*\d:[0-5]\d"
    if re.match(pattern, start_time):
        converted_time = convert_time(start_time)
        if 0 <= converted_time < 1440:
            return True


def valid_end_time(start_time, end_time):
    if valid_start_time(start_time) and valid_start_time(end_time):
        if convert_time(end_time) > convert_time(start_time):
            return True
        print("End time must be after start time.")


def get_job():
    job_name = input("Enter job name (case sensitive): ")
    start_time = ""
    while not valid_start_time(start_time):
        start_time = input("Enter start time (hh:mm): ")
    end_time = ""
    while not valid_end_time(start_time, end_time):
        end_time = end_time = input("Enter end time (hh:mm): ")
    job = [job_name, start_time, end_time]
    return job
    

def add_to_list(job):
    """Add job to jobs.csv."""
    job = get_job()
    with open("job_scheduler/jobs.csv", "a") as f:
        csv_writer = writer(f)
        csv_writer.writerow(job)


def add_to_tree(job, tree):
    start_time = convert_time(job[1])
    end_time = convert_time(job[2])
    return tree.insert(job, start_time, end_time)


def remove_job(tree):
    """remove job from jobs.csv and job tree"""
    # TODO: must be a better way
    job = get_job()
    job_removed = False
    new_job_list = []
    
    with open("job_scheduler/jobs.csv") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            if row == job:
                job_removed = True
                tree.delete(job)
            else:
                new_job_list.append(row)

    with open("job_scheduler/jobs.csv", "w") as f:
        csv_writer = writer(f)
        for job in new_job_list:
            csv_writer.writerow(job)

    if job_removed:
        print("Job removed.")
    else:
        print("Job not found. Removal not performed.")


def print_in_order(tree):
    print("Today's schedule:")
    print("---------------------------------")
    tree.in_order()

#---------------------------------------------------#

job_tree = BinarySearchTree()
a = add_to_tree(["wah","12:00","13:00"], job_tree)
b = add_to_tree(["spam","13:00","14:00"], job_tree)

print(a)
print(b)

# print("\nJOB SCHEDULER")
# print("=============\n")
# print("Loading jobs.csv...")

# with open("job_scheduler/jobs.csv") as f:
#     jobs = reader(f)
#     job_list = [job for job in jobs]

# print("Building job schedule...")

# successes = []
# fails = []
# job_tree = BinarySearchTree()
# for job in job_list:
#     if add_to_tree(job, job_tree):
#         successes.append(job)
#     else:
#         fails.append(job)

# print()
# print("Successfully added:")
# print(successes)
# print()
# print("Not added due to time slot conflicts:")
# print(fails)
# print()

# running = True
# # TODO: add error handling
# while running:
#     user_input = input("""What would you like to do? Press:
# 1 to view today's schedule
# 2 to add a job
# 3 to remove a job
# 4 to quit
# -> """)
#     if user_input == "1":
#         print()
#         print_in_order(job_tree)
#     elif user_input == "2":
#         print()
#         add_job(job_tree)
#         print()
#     elif user_input == "3":
#         print()
#         remove_job(job_tree)
#         print()
#     elif user_input == "4":
#         print()
#         running = False
#     else:
#         print()
#         print("Invalid input.")
#         print()
