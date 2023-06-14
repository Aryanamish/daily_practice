class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:

    def __str__(self):
        l = []
        curr = self.head
        while curr is not None:
            l.append(curr.data)
            curr = curr.next
        l.reverse()
        return str(l)

    def __repr__(self):
        return self.__str__()

    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, value):
        node = Node(value, self.head)
        self.head = node
        self.length += 1

    @property
    def isEmpty(self):
        return self.length == 0

    def peek(self):
        return self.head.data if self.head is not None else None

    def pop(self):
        if self.head is not None:
            val = self.head.data
            self.head = self.head.next
            self.length -= 1
            return val
        return None