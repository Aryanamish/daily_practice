class Solution:
    def splitArraySameAverage(self, nums):
        return self.rec(nums, len(nums)-1, [], [], 0, 0)
    
    def rec(self, nums, n, setA, setB, sumA, sumB):
        if n == -1:
            try:
                ans = sum(setA)/len(setA) == sum(setB)/len(setB)
                if ans is True:
                    print(setA, setB)
                return ans
            except:
                return False
        
        setA.append(nums[n])
        if self.rec(nums, n-1, setA, setB, sumA + nums[n], sumB):
            return True
        setA.pop()

        setB.append(nums[n])
        if self.rec(nums, n-1, setA, setB, sumA, sumB + nums[n]):
            print(setA, setB)
            return True
        setB.pop()

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))