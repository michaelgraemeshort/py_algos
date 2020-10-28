# do docstrings, unit tests

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes:
            nodes = [Node(i) for i in nodes]
            self.head = nodes[0]
            self.tail = nodes[-1]
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            for i in range(len(nodes) - 1, 0, -1):
                nodes[i].previous = nodes[i - 1]

    def __getitem__(self, index):
        return self.get(index)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        if not self.head:
            return length
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def __str__(self):
        if not self.head:
            return "list is empty"
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def get(self, index):
        if not self.head:
            return "list is empty"
        if index >= 0:
            node = self.head
            for i in range(index):
                node = node.next
                if not node:
                    raise IndexError("list index out of range")
            return node
        node = self.tail
        for i in range(abs(index) - 1):
            node = node.previous
            if not node:
                raise IndexError("list index out of range")
        return node

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.last = new_node
            return
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def add_after(self, target_node_data, new_data):
        new_node = Node(new_data)
        node = self.head
        while node and node.data != target_node_data:
            node = node.next
        if not node:
            raise Exception("target node not found. data not added")
        new_node.next = node.next
        if new_node.next:
            node.next.previous = new_node
        else:
            self.tail = new_node
        node.next = new_node
        new_node.previous = node

    def add_before(self, target_node_data, new_data):
        new_node = Node(new_data)
        node = self.head
        while node and node.data != target_node_data:
            node = node.next
        if not node:
            raise Exception("target node not found. data not added")
        new_node.next = node
        if node.previous:
            new_node.previous = node.previous
            node.previous.next = new_node
        else:
            self.head = new_node
        node.previous = new_node

    def remove_first(self):
        if not self.head:
            return "list is empty"
        node = self.head
        if not node.next:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            self.head.previous = None

    def remove_last(self):
        if not self.head:
            return "list is empty"
        node = self.tail
        if not node.previous:
            self.head = None
            self.tail = None
        else:
            self.tail = node.previous
            self.tail.next = None

    def remove_node(self, target_node_data):
        if not self.head:
            return "list is empty"
        node = self.head
        while node and target_node_data != node.data:
            node = node.next
        if not node:
            raise Exception("target not found")
        if not node.previous and not node.next: # if target node is only node
            self.head = None
            self.tail = None
            return
        if not node.previous:   # if target node is head node
            self.head = node.next
            self.head.previous = None
            return
        if not node.next:   # if target node is tail node
            self.tail = node.previous
            self.tail.next = None
            return
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

    def reverse_list(self):
        if not self.head:
            return "list is empty"
        self.head, self.tail = self.tail, self.head
        for node in self:
            node.next, node.previous = node.previous, node.next

            
# dll = DoublyLinkedList(list("abcd"))
dll = DoublyLinkedList(["a", 1, {"b"}, [2], {3: "three"}])
dll.reverse_list()
print("dll:", dll)
print("head:", dll.head)
print("tail:", dll.tail)
