# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        
        a = self.inorderleft(root.left) 
        b = self.inorderright(root.right)
        if a == b:
            return True
        return False
    
    def inorderleft(self, root):
        if root:
            val = ''
            if root.left is not None:
                val += f"L{self.inorderleft(root.left)}"
            val += str(root.val)
            if root.right is not None:
                val += f"R{self.inorderleft(root.right)}"
            return val
    
    def inorderright(self, root):
        if root:
            val = ''
            if root.right is not None:
                val += f"L{self.inorderright(root.right)}"
            val += str(root.val)

            if root.left is not None:
                val += f"R{self.inorderright(root.left)}"
            return val