class Solution:
    def containsDuplicate(self, nums):
        found = set(nums)
        for i in nums:
            if i in found:
                return False
            else:
                found.add(i)
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))