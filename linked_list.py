class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(i)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:  # empty 
            self.head = node
            return
        for i in self:
            pass
        i.next = node

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)  # this is of course a STRING METHOD so node data must be STRINGS


linked_list = LinkedList(["1", "2", "3"])

print(linked_list)
linked_list.add_first(Node("7"))
print(linked_list)
linked_list.add_last(Node("8"))
print(linked_list)