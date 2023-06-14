class Solution:

    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        new = [(nums[i], i) for i in range(len(nums))]
        new.sort()
        ans = 0
        i = 0
        while i < len(nums):
            swap = new[i][1]
            if swap != i:

                new[i], new[swap] = new[swap], new[i]
                ans += 1
            else:
                i += 1
        return ans


#{
# Driver Code Starts

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)

# } Driver Code Ends