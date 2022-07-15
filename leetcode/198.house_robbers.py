import numpy
import random
class Solution:
    def max(self, first, second):
        return first if first > second else second
        
    def rob(self, nums) -> int:
        print(nums)
        length = len(nums)
        max_money = numpy.empty(length, dtype=int)
        if length == 0:
            return 0

        max_money[0] = nums[0]
        max_money[1] = self.max(nums[0], nums[1])
        
        for i in range(2, length):
            max_money[i] = self.max(nums[i] + max_money[i-2], max_money[i-1])
        print(max_money)
        return max_money[-1]

s = Solution()
print(s.rob([random.randint(0,200) for _ in range(10)]))