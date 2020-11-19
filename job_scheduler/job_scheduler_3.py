

from classes2 import Node, BinarySearchTree
from csv import reader, writer
import re


def convert_time(time):
    """convert time from hh:dd to minutes after 00:00"""
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)


def get_job():
    """return job, given valid input. otherwise, return None"""
    job_name = input("Enter job name (case sensitive): ")
    start_time = input("Enter start time (hh:mm): ")
    pattern = r"[0-2]*\d:[0-5]\d"
    if not re.match(pattern, start_time):
        print("\nERROR: invalid input.")
        return
    converted_start_time = convert_time(start_time)
    if converted_start_time > 1439:
        print("\nERROR: invalid time.")
        return
    end_time = input("Enter end time (hh:mm): ")
    if not re.match(pattern, end_time):
        print("\nERROR: invalid input.")
        return
    converted_end_time = convert_time(end_time)
    if converted_end_time > 1439:
        print("\nERROR: invalid time.")
        return
    elif converted_end_time == 0:
        converted_end_time = 1440
    if not converted_start_time < converted_end_time:
        print("\nERROR: end time must be after start time.")
        return
    job = [job_name, start_time, end_time, converted_start_time, converted_end_time]
    return job


def add_job(tree):
    """Add job to job tree and, if successful, jobs.csv."""
    job = get_job()
    if job:
        if tree.insert(job):
            with open("job_scheduler/jobs.csv", "a") as f:
                csv_writer = writer(f)
                csv_writer.writerow(job[:3])
            print(f"\n{job[0]} inserted successfully.")
        else:
            print(f"\n***{job[0]} NOT inserted due to time slot conflict.***")


def remove_job(tree):
    """remove job from job tree and, if successful, jobs.csv."""
    job = get_job()
    if job:
        if tree.delete(job):
            print(f"\n{job[0]} removed successfully.")
            new_job_list = []

            with open("job_scheduler/jobs.csv") as f:
                csv_reader = reader(f)
                for row in csv_reader:
                    if row != job[:3]:
                        new_job_list.append(row)

            with open("job_scheduler/jobs.csv", "w") as f:
                csv_writer = writer(f)
                for job in new_job_list:
                    csv_writer.writerow(job[:3])

        else:
            print(f"\nERROR: {job[0]} ({job[1]} - {job[2]}) not found.")


def print_in_order(tree):
    print("Today's schedule:")
    print("---------------------------------")
    tree.in_order()

#---------------------------------------------------#

print("\nJOB SCHEDULER")
print("=============\n")
print("Loading jobs.csv...")

with open("job_scheduler/jobs.csv") as f:
    jobs = reader(f)
    job_list = [job for job in jobs]

print("Building job schedule...\n")

job_tree = BinarySearchTree()

for job in job_list:
    job.extend([convert_time(job[1]), convert_time(job[2])])
    job_tree.insert(job)

running = True
while running:
    user_input = input("""What would you like to do? Press:
1 to view today's schedule
2 to add a job
3 to remove a job
4 to quit
-> """)
    if user_input == "1":
        print()
        print_in_order(job_tree)
    elif user_input == "2":
        print()
        add_job(job_tree)
        print()
    elif user_input == "3":
        print()
        remove_job(job_tree)
        print()
    elif user_input == "4":
        print()
        running = False
    else:
        print()
        print("ERROR: invalid input.")
        print()
