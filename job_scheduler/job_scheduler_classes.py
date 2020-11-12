class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self, data=None):
        self.root = None
        if data:
            for i in data:
                self.insert(i)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if not node.left_child:
                node.left_child = Node(data)
            else:
                self._insert(node.left_child, data)
        elif data > node.data:
            if not node.right_child:
                node.right_child = Node(data)
            else:
                self._insert(node.right_child, data)

    def in_order(self):
        self._in_order(self.root)
        print()

    def _in_order(self, node):
        if node:
            self._in_order(node.left_child)
            print(node, end=" ")
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
            elif value < node.data:
                self._delete(node.left_child, node, True, value)
            elif value > node.data:
                self._delete(node.right_child, node, False, value)
        else:
            raise ValueError(f"{value} not in tree")
