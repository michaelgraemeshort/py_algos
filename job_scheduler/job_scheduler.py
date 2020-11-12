from classes import Node, BinarySearchTree
from csv import reader, writer


def convert_time(time):
    """convert time from hh:dd to minutes after 00:00"""
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)


def get_job():
    # TODO: add error handling
    job_name = input("Enter job name (case sensitive): ")
    start_time = input("Enter start time (hh:mm): ")
    end_time = input("Enter end time (hh:mm): ")
    job = [job_name, start_time, end_time]
    return job
    

def add_job(tree):
    """Add job to jobs.csv and job tree."""
    job = get_job()
    with open("job_scheduler/jobs.csv", "a") as f:
        csv_writer = writer(f)
        csv_writer.writerow(job)
    tree.insert(job)


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

print("\nJOB SCHEDULER")
print("=============\n")
print("Loading jobs.csv...")

with open("job_scheduler/jobs.csv") as f:
    jobs = reader(f)
    job_list = [job for job in jobs]

print("Building job schedule...\n")

job_tree = BinarySearchTree()
for job in job_list:
    job_tree.insert(job)

print()

running = True
# TODO: add error handling
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
