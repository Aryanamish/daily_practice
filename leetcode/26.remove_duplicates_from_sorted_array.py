class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[k]:
                continue
            else:
                nums[k+1] = nums[i]
                k+=1
        return k+1

    def removeDuplicates2(self, nums) -> int:
        num2 = list(set(nums))
        k = len(num2)
        nums[:k] = num2
        return k



if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,3,4,4,5,5,6,6,7,7]))
    print(s.removeDuplicates([1,1,2]))