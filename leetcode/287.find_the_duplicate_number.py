class Solution:
    def findDuplicate(self, nums):
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1

        while low <= high:
            cur = (low + high) // 2
            print(f'{low=}, {cur=}, {high=}')
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1

        return duplicate

    def findDuplicate2(self, nums):
        while nums[0] != nums[nums[0]]:
            nums[0], nums[nums[0]] = nums[nums[0]], nums[0]
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate2([5, 5, 4, 1, 3, 2]))
