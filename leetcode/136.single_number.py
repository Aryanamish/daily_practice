class Solution:
    def alternate_sol(self, nums):
        found = set()
        for i in nums:
            if i in found:
                found.remove(i)
                continue
            if i not in found:
                found.add(i)
        return found.pop()

    def singleNumber(self,nums):
        return (2*sum(set(nums))) - sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1]))