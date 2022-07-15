# Definition for a binary tree node.
import parent
from datastructure.binary_tree import BinaryTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.val)
            self.inorderTraversal(root.right)