class Solution:
    def maxSubArray(self, nums) -> int:
        last = largest_sum = nums[0]
        for num in nums[1:]:
            last = max(last + num, num)
            largest_sum = max(largest_sum, last)
        return largest_sum

# largest_sum_till_now = 6
# i = 8
if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1,3,4,6]))