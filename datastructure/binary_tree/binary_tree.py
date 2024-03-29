import json
import random

count = 0
common_value = []
class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.val = value
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"{self.left.val if self.left is not None else 'None'} <-- {self.val} --> {self.right.val if self.right is not None else 'None'}"
    
    def __repr__(self) -> str:
        return f"{self.left.val if self.left is not None else 'None'} <-- {self.val} --> {self.right.val if self.right is not None else 'None'}"

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> None:
        new_node = Node(value)
        if self.root is not None:
            current_node = self.root
            while True:
                if current_node.val == value:
                    break
                elif current_node.val is not None:
                    if current_node.val > value:
                        if current_node.left is None:
                            current_node.left = new_node
                            break
                        else:
                            current_node = current_node.left
                    elif current_node.val < value:
                        if current_node.right is None:
                            current_node.right = new_node
                            break
                        else:
                            current_node = current_node.right
                else:
                    current_node.val = value
                    break
        else:
            self.root = new_node

    def lookup(self, value):
        current_node = self.root
        while current_node is not None and current_node.val != value:
            if value < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return current_node or False

    def traverse(self, node):
        if node is not None:
            tree = {'value': node.val}
            tree['left'] = None if node.left is None else self.traverse(node.left)
            tree['right'] = None if node.right is None else self.traverse(node.right)
            return tree
        return {}


    def __str__(self) -> str:
        return json.dumps(self.traverse(self.root))

if __name__ == '__main__':
    bt  = BinaryTree()
    for i in range(0,200): 
        value = int(random.randint(0,2))
        common_value.append(value)
        bt.insert(value)
        count = count + 1
    print(bt)
    print(bt.lookup(120))
