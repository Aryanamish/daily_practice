import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    min_depth = float('inf')
    
    def minDepth(self, root):
        return self.find_depth()


    def find_depth(self,node):
        q = queue.Queue()
        q = q.set(node.left, node.right)

        if node is not None:
            self.find_depth(node.left)
        