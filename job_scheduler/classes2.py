class Node:
    """node for BinarySearchTree"""
    def __init__(self, data):
        self.data = data
        self.job_name = data[0]
        self.start_time = data[3]
        self.end_time = data[4]
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Job:\t\t{self.data[0]}\nStart time:\t{self.data[1]}\nEnd time:\t{self.data[2]}\n"


class BinarySearchTree:
    def __init__(self, data=None):
        self.root = None

    def insert(self, data):
        """return True on successful insertion"""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return True
        return self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.end_time <= current.start_time:
            if not current.left_child:
                current.left_child = new_node
                return True
            else:
                return self._insert(current.left_child, new_node)
        elif new_node.start_time >= current.end_time:
            if not current.right_child:
                current.right_child = new_node
                return True
            else:
                return self._insert(current.right_child, new_node)

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
        """returns True on successful deletion"""
        return self._delete(self.root, None, None, data)

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
                            return True
                        else:    
                            parent.right_child = None
                            return True
                    # if root
                    else:
                        self.root = None
                        return True
                # if left child only
                elif current.left_child and not current.right_child:
                    # if not root
                    if parent:
                        if is_left:
                            parent.left_child = current.left_child
                            return True
                        else:
                            parent.right_child = current.left_child
                            return True
                    # if root
                    else:
                        self.root = current.left_child
                        current.left_child = None
                        return True
                # if right child only
                elif not current.left_child and current.right_child:
                    # if not root
                    if parent:
                        if is_left:
                            parent.left_child = current.right_child
                            return True
                        else:
                            parent.right_child = current.right_child
                            return True
                    # if root
                    else:
                        self.root = current.right_child
                        current.right_child = None
                        return True
                # if two children
                else:
                    # get data of leftmost value of right subtree
                    min_right_subtree_data = self.min_right_subtree(current)
                    # delete node with that data (has at most one child so handled by above)
                    self.delete(min_right_subtree_data)
                    # replace current node data with that data
                    current.data = min_right_subtree_data
                    return True
            # if node is to left
            elif target_node.end_time <= current.start_time:
                # move left
                return self._delete(current.left_child, current, True, data)
            # if node is to right
            elif target_node.start_time >= current.end_time:
                # move right
                return self._delete(current.right_child, current, False, data)
