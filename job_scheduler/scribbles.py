class Node:
    def __init__(self, data):
        self.data = data
        self.start_time_24h = data[0]
        self.duration = data[1]
        self.job_name = data[2]
        self.start_time = data[3]
        self.end_time = data[4]
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Task name:\t\t{self.job_name}\nStart time:\t\t{self.start_time_24h}\nDuration (minutes):\t{self.duration}\n"


class BinarySearchTree:
    def __init__(self, data=None):
        self.root = None
        if data:
            for i in data:
                self.insert(i)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            print(f"{data[2]} added sucessfully.")
            return
        self._insert(self.root, data)

    def _insert(self, node, data):
        if data[4] <= node.start_time:
            if not node.left_child:
                node.left_child = Node(data)
                print(f"{data[2]} added sucessfully.")
            else:
                self._insert(node.left_child, data)
        elif data[3] >= node.end_time:
            if not node.right_child:
                node.right_child = Node(data)
                print(f"{data[2]} added sucessfully.")
            else:
                self._insert(node.right_child, data)
        else:
            print(f"***{data[2]} NOT added due to time slot conflicts.***")

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left_child)
            print(node)
            self._in_order(node.right_child)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node:
            if value == node.data:
                return f"{value} IS in tree"    # this is lame
            elif value > node.data:
                return self._find(node.right_child, value)
            else:
                return self._find(node.left_child, value)
        raise ValueError(f"{value} not in tree")

    def __contains__(self, value):
        if not self.root:
            return False
        node = self.root
        while node:
            if value == node.data:
                return True
            elif value < node.data:
                node = node.left_child
            else:
                node = node.right_child
        return False

    def min_right_subtree(self, node):
        node = node.right_child
        while node.left_child:
            node = node.left_child
        return node.data

    def delete(self, value):
        self._delete(self.root, None, None, value)

    def _delete(self, node, parent, is_left, value):
        # FIX THIS
        if node:
            if value == node.data:
                if not node.left_child and not node.right_child:
                    if parent:
                        if is_left:
                            parent.left_child = None
                        else:    
                            parent.right_child = None
                    else:
                        self.root = None
                elif node.left_child and not node.right_child:
                    if parent:
                        if is_left:
                            parent.left_child = node.left_child
                        else:
                            parent.right_child = node.left_child
                    else:
                        self.root = node.left_child
                        node.left_child = None
                elif not node.left_child and node.right_child:
                    if parent:
                        if is_left:
                            parent.left_child = node.right_child
                        else:
                            parent.right_child = node.right_child
                    else:
                        self.root = node.right_child
                        node.right_child = None
                else:
                    min = self.min_right_subtree(node)
                    self.delete(min)
                    node.data = min
            elif value[4] < node.start_time:
                self._delete(node.left_child, node, True, value)
            elif value[3] > node.end_time:
                self._delete(node.right_child, node, False, value)
        else:
            raise ValueError(f"{value} not in tree")


tree = BinarySearchTree()

from csv import reader

def convert_time(twenty_four_hour_time):
    """convert time from hh:dd to minutes after 00:00"""
    hours, minutes = twenty_four_hour_time.split(":")
    return int(hours) * 60 + int(minutes)

def convert_job(job):
    """make job ready to pass to Node"""
    job.append(convert_time(job[0]))
    job.append(job[3] + int(job[1]))
    return job

with open("job_scheduler/jobs.csv") as f:
    jobs = reader(f)
    job_list = [job for job in jobs]

for job in job_list:
    tree.insert(convert_job(job))

print(job_list)

tree.in_order()
tree.delete(convert_job(job_list[0]))
tree.in_order()