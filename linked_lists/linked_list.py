
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            self.head = Node(nodes.pop(0))
            node = self.head
            while nodes:
                node.next = Node(nodes.pop(0))
                node = node.next

    def __str__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

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

    def __getitem__(self, i):   # maybe refactor this and get(self, i)
        if i >= 0:
            return self.get(i)
        if -(len(self)) <= i < 0:
            return self.get(len(self) + i)
        raise IndexError("list index out of range")

    def get(self, i):
        if not self.head:
            raise Exception("list is empty")
        node = self.head
        for _ in range(i):
            node = node.next
            if not node:
                raise IndexError("list index out of range")
        return node.data

    def get_index(self, target_node_data):
        if not self.head:
            raise Exception("list is empty")
        i = 0
        node = self.head
        while node:
            if node.data == target_node_data:
                return i
            i += 1
            node = node.next
        raise ValueError(f"{target_node_data} is not in list")             

    def add_first(self, s): # takes a string, not a node
        new_node = Node(s)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, s):
        new_node = Node(s)
        if not self.head:
            self.head = new_node
        else:
            for i in self:
                pass
            i.next = new_node

    def add_after(self, target_node_data, s):   # adds after the FIRST occurrence of target_node_data
        if not self.head:
            raise Exception("list is empty")
        new_node = Node(s)
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return  # otherwise, errors in case of further occurrences
        raise Exception(f"node with data \"{target_node_data}\" not found")

    def add_before(self, target_node_data, s):  # adds before the FIRST occurrence of target_node_data
        if not self.head:
            raise Exception("list is empty")
        new_node = Node(s)
        if self.head.data == target_node_data:
            # THIS DOESN'T WORK
            # add_first(self, s)
            # THIS DOES
            self.add_first(s)
            return
            # WHICH IS BETTER EXPRESSED AS
            # return self.add_first(s)
            # AND THIS IS JUST A BIT WET
            # new_node.next = self.head
            # self.head = new_node
            # return
        for node in self:
            if node.next:
                if node.next.data == target_node_data:
                    node_after = node.next
                    node.next = new_node
                    new_node.next = node_after
                    return
        raise Exception(f"node with data \"{target_node_data}\" not found.")

    def remove_first(self):
        if not self.head:
            raise Exception("list is empty")
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            raise Exception("list is empty")
        node = self.head
        # if no second node:
        if not node.next:
            # remove first node
            self.head = None
            return
        # if no third node:
        if not node.next.next:
            # remove second node
            node.next = None
            return        
        while node.next.next:
            node = node.next
        node.next = None

    def remove_by_data(self, target_node_data):
        if not self.head:
            raise Exception("list is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        for node in self:
            if node.next:
                next_node = node.next
                if next_node.data == target_node_data:
                    node.next = next_node.next
                    return
        raise Exception(f"node with data \"{target_node_data}\" not found")

    def remove_by_index(self, i):
        if not self.head:
            raise Exception("list is empty")
        if i == 0:
            self.head = self.head.next
            return
        node = self.head
        # go to the index BEFORE the one specified
        # connect node at that index with the one AFTER the one it is currently connected to
        # if it exists
        for _ in range(i - 1):
            node = node.next
            if not node.next:
                raise IndexError("list index out of range")
        node.next = node.next.next

    def reverse_list(self):
        if not self.head:
            raise Exception("list is empty")
        node = self.head
        next_node = node.next
        # point node at None instead of next_node
        node.next = None
        # while next_node is not None:
        while next_node:
            # create reference to third node before redirecting second at first
            node_after_next = next_node.next
            # point second node at first
            next_node.next = node
            # make second node the new head
            self.head = next_node
            # reassign node and next_node for the next iteration
            # which will only run if there is a node_after_next
            node = next_node
            next_node = node_after_next

class Queue(LinkedList):
    def __init__(self, nodes=None):
        super().__init__(nodes)

    def enqueue(self, s):
        return self.add_last(s)

    def dequeue(self):
        return self.remove_first()


ll = LinkedList(["a", "b", "c", "d"])
empty_ll = LinkedList()
ll.remove_by_index(5)
print(ll)