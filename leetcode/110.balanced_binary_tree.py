# Definition for a binary tree node.
import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        data = []
        q = queue.Queue()
        q.put(self)
        while q.empty() is not True:
            node = q.get()
            if node is not None:
                q.put(node.left)
                q.put(node.right)
                data.append(node.val)
            else:
                data.append(node)
        return str(data)
    
    def __repr__(self) -> str:
        return self.__str__()


        


class Solution:

    def check_depth(self, root, height=0):
        left = right = 0
        if root is not None:
            if root.right is not None:
                right = self.check_depth(root.right, height+1)
            if root.left is not None:
                left = self.check_depth(root.left, height+1)
            height = max(right, left, height)
        return height

        

    def isBalanced(self, root):
        if root is not None:
            left = right = 0
            if root.left is not None:
                left = self.check_depth(root.left) + 1
            if root.right is not None:
                right = self.check_depth(root.right) + 1
        else:
            return True
        return True if abs(left - right) <= 1 else False


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(3,TreeNode(9), TreeNode(20,TreeNode(15),TreeNode(7)))
    tree2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    print(tree2)
    print(s.isBalanced(tree2))
