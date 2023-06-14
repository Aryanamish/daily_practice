#User function Template for python3


class isBst:

    def __init__(self,
                 is_bst,
                 total_node=1,
                 min=float('-inf'),
                 max=float('inf')):
        self.bst = is_bst
        self.length = total_node
        self.min = min
        self.max = max

    def __str__(self):
        return str(self.bst) + ', ' + str(self.length) + ', ' + str(
            self.min) + ', ' + str(self.max)


class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        #code here
        no_of_node = [0]

        def rec(node):
            if node.left is None and node.right is None:
                return isBst(True, 1, node.data, node.data)

            left = rec(node.left) if node.left else isBst(
                True, 0, node.data, node.data - 1)
            right = rec(node.right) if node.right else isBst(
                True, 0, node.data + 1, node.data)
            if left.bst and right.bst:
                if left.max < node.data < right.min:
                    return isBst(True, left.length + right.length + 1,
                                 left.min, right.max)

            return isBst(False, max(left.length, right.length))

        return rec(root).length

    def check_bst(self, root, no_of_node, low=float('-inf'),
                  high=float('inf')):
        if root is None:
            return True
        no_of_node[0] += 1
        if not low < root.data < high:
            return False

        return (self.check_bst(root.left, no_of_node, low, root.data)
                and self.check_bst(root.right, no_of_node, root.data, high))


#{
# Driver Code Starts
import sys

sys.setrecursionlimit(1000000)

from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = 1
    for _ in range(0, t):
        s = "6 6 3 N 2 9 3 N 8 8 2"

        root = buildTree(s)
        ob = Solution()
        print(ob.largestBst(root))

# } Driver Code Ends