class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

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
        pass

    def _in_order(self, node):
        pass

    def pre_order(self):
        pass

    def _pre_order(self, node):
        pass

    def post_order(self):
        pass

    def _post_order(self, node):
        pass


bst = BinarySearchTree()
bst.insert(5)
print(bst.root)
bst.insert(4)
print(bst.root.left_child)
bst.insert(8)
print(bst.root.right_child)
bst.insert(3)
print(bst.root.left_child)
print(bst.root.left_child.left_child)
bst.insert(9)
print(bst.root.right_child)
print(bst.root.right_child.right_child)