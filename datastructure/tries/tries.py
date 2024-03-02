class Node:
    def __init__(self, value):
        self.val = value
        self.next = {}

class Tries:
    def __init__(self):
        self.root = Node()