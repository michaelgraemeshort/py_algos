def convert_time(time):
    """convert time from hh:dd to minutes after 00:00"""
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)

class Node:
    def __init__(self, data):
        self.data = data
        self.job_name = data[0] # BEWARE - this doesn't update if data is updated
        self.start_time = convert_time(data[1])
        self.end_time = convert_time(data[2])
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Job:\t\t{self.data[0]}\nStart time:\t{self.data[1]}\nEnd time:\t{self.data[2]}\n"


class BinarySearchTree:
    def __init__(self, data=None):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            print(f"{new_node.job_name} added sucessfully.")
            return
        self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.end_time <= current.start_time:
            if not current.left_child:
                current.left_child = new_node
                print(f"{new_node.job_name} added sucessfully.")
            else:
                self._insert(current.left_child, new_node)
        elif new_node.start_time >= current.end_time:
            if not current.right_child:
                current.right_child = new_node
                print(f"{new_node.job_name} added sucessfully.")
            else:
                self._insert(current.right_child, new_node)
        else:
            print(f"***{new_node.job_name} NOT added due to time slot conflicts.***")

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left_child)
            print(node)
            self._in_order(node.right_child)

    def min_right_subtree(self, node):
        node = node.right_child
        while node.left_child:
            node = node.left_child
        return node.data

    def delete(self, data):
        self._delete(self.root, None, None, data)

    def _delete(self, current, parent, is_left, data):
        target_node = Node(data)
        if current:
            if target_node.data == current.data:
                # if no children
                if not current.left_child and not current.right_child:
                    # if not root
                    if parent:
                        if is_left:
                            parent.left_child = None
                        else:    
                            parent.right_child = None
                    # if root
                    else:
                        self.root = None
                # if left child only
                elif current.left_child and not current.right_child:
                    # if not root
                    if parent:
                        if is_left:
                            parent.left_child = current.left_child
                        else:
                            parent.right_child = current.left_child
                    # if root
                    else:
                        self.root = current.left_child
                        current.left_child = None
                # if right child only
                elif not current.left_child and current.right_child:
                    # if not root
                    if parent:
                        if is_left:
                            parent.left_child = current.right_child
                        else:
                            parent.right_child = current.right_child
                    # if root
                    else:
                        self.root = current.right_child
                        current.right_child = None
                # if two children
                else:
                    # get data of leftmost value of right subtree
                    min_right_subtree_data = self.min_right_subtree(current)
                    # delete node with that data (has at most one child so handled by above)
                    self.delete(min_right_subtree_data)
                    # replace current node data with that data
                    current.data = min_right_subtree_data
            # if node is to left
            elif target_node.end_time <= current.start_time:
                # move left
                self._delete(current.left_child, current, True, data)
            # if node is to right
            elif target_node.start_time >= current.end_time:
                # move right
                self._delete(current.right_child, current, False, data)
        # if current == None
        else:
            raise ValueError(f"{target_node.job_name} not in job tree")
