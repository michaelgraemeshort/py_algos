class Node:
    """Node for singly-linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    """Singly-linked list with tail."""

    def __init__(self, nodes=None):  # nodes is a list. must learn type hints
        self.head = None
        self.head = None
        if nodes:
            node = Node(nodes[0])
            self.head = node
            for i in nodes[1:]:
                node.next = Node(i)
                node = node.next
            self.tail = node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def __getitem__(self, n):
        """Returns the value at the nth index from the beginning of the list."""
        if not self.head:
            raise IndexError("list is empty")
        if n < 0:
            raise IndexError("cannot index by negative number")
        node = self.head
        for i in range(n):
            node = node.next
            if not node:
                raise IndexError("list index out of range")
        return node.data

    def __delitem__(self, n):
        """Deletes the value at the nth index from the beginning of the list."""
        if not self.head:
            raise IndexError("list assignment index out of range")
        if n < 0:
            raise IndexError("cannot index by negative number")
        if n == 0:
            return self.popleft()
        node = self.head
        for i in range(n):
            if node.next:
                previous_node = node
                node = node.next
            else:
                raise IndexError("list assignment index out of range")
        if not node.next:
            return self.pop()
        previous_node.next = node.next             

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

    def append(self, element):
        """Add an element to the right side of the list."""
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def appendleft(self, element):
        """Add an element to the left side of the list."""
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, element):
        """Insert element before index."""
        if index < 0:
            raise IndexError("cannot index by negative number")
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if not index:
            return self.appendleft(element)
        node = self.head
        for i in range(index - 1):
            if node.next:
                node = node.next
        if not node.next:
            return self.append(element)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, target_value, element):
        """
        Insert element before target value.
        
        Raise ValueError if the target value is not present.
        """
        if not self.head:
            raise ValueError(f"{target_value} not in list")
        node = self.head
        if node.data == target_value:
            return self.appendleft(element)
        while node.next:
            if node.next.data == target_value:
                new_node = Node(element)
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
        raise ValueError(f"{target_value} not in list")

    def insert_after(self, target_value, element):
        """
        Insert element after target value.
        
        Raise ValueError if the target value is not present.
        """
        if not self.head:
            raise ValueError(f"{target_value} not in list")
        node = self.head
        while node:
            if node.data == target_value:
                new_node = Node(element)
                if not node.next:
                    return self.append(new_node)
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
        raise ValueError(f"{target_value} not in list")       
        
    def pop(self):
        """Remove and return the rightmost element."""
        if not self.head:
            raise IndexError("pop from empty list")
        node = self.head
        # if one item list:
        if not node.next:
            self.head = None
            self.tail = None
            return node
        # while the next node has a next node:
        while node.next.next:
            # iterate through nodes. stop when node is penultimate node
            node = node.next
        # create reference to last node
        last_node = node.next
        # remove last node from list
        node.next = None
        self.tail = node
        return last_node

    def popleft(self):
        """Remove and return the leftmost element."""
        if not self.head:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        return node

    def remove(self, value):
        """
        Remove first occurrence of value.
        
        Raise ValueError if the value is not present.
        """
        if not self.head:
            raise ValueError(f"{value} not in list")
        node = self.head
        if node.data == value:
            return self.popleft()
        # while there is a next node
        while node.next:
            # if that node is THE node
            if node.next.data == value:
                # and that node is also the tail
                if not node.next.next:
                    return self.pop()
                # otherwise
                node.next = node.next.next
                return
            # otherwise            
            node = node.next
        raise ValueError(f"{value} not in list")

    def reverse(self):
        """Reverse *IN PLACE*."""
        if not self.head:
            return
        node = self.head
        self.tail = node
        if not node.next:
            return
        next_node = node.next
        # redirect node's pointer
        node.next = None
        while next_node:
            # create reference to node after next
            node_after_next = next_node.next
            # redirect next_node's pointer
            next_node.next = node
            self.head = next_node
            # reassign next_node and node for next iteration of loop
            node = next_node
            next_node = node_after_next
        
    def reverse_recursively(self, node, previous_node=None):
        """Reverse *IN PLACE*. Pass self.head in."""
        if not self.head:
            return
        if not node.next:
            self.tail = self.head
            self.head = node
            node.next = previous_node
        else:
            next_node = node.next
            node.next = previous_node
            self.reverse_recursively(next_node, node)
