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

class BinaryTree:

    def __init__(self, val=0) -> None:
        self.root = TreeNode(val)
    
    def convert_list(self, tree):
        q = queue.Queue()
        q.put(self.root)
        i = 0
        while q.empty() is False and i < len(tree):
            node = q.get()
            node.val = tree[i]
            node.left = TreeNode(0)
            node.right = TreeNode(0)
            q.put(node.left)
            q.put(node.right)
            i += 1
        node.left == None
        node.right == None


class Solution:
    target = 0
    target_found = False

    def hasPathSum(self, root, targetSum):
        self.target = targetSum
        self.cal_sum(root, 0)
        return self.target_found

    def cal_sum(self, node, sum):

        if node is None:
            return 0
        else:
            if node.right is None and node.left is None and sum == self.target:
                self.target_found = True
                return 0
            sum += node.val or 0
            self.cal_sum(node.right, sum)
            if self.target_found is True:
                return 0
            self.cal_sum(node.left, sum)
        return 0

        
if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree()
    tree.convert_list([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(tree.root)
    ans = s.hasPathSum(tree.root, 22)
    print(ans)