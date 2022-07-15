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


class Solution:
    def sortedArrayToBST(self, nums):
        if nums is not None:
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            middle,left, right = self.split(nums)
            
            return TreeNode(middle, self.sortedArrayToBST(left), self.sortedArrayToBST(right))
        return

        
    def split(self, nums):
        if len(nums) == 0:
            return None, None, None
        middle = len(nums)//2 
        left, right, middle = nums[:middle] , nums[middle+1:], nums[middle]
        return middle, left if len(left) > 0 else None, right if len(right) > 0 else None


if __name__ == '__main__':
    s = Solution()
    tree = s.sortedArrayToBST([-10,-3,0,5,9])
    print(tree)
