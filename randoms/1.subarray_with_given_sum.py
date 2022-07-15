class Solution:
    def subArraySum(self,arr, n, s): 
        i,j = 0,0
        sum=0
        while i<n and j<n:
            if s == sum:
                return [j+1, i]
                break
            elif sum < s:
                sum += arr[i]
                i += 1
            elif sum > s:
                sum -= arr[j]
                j +=1
                i -= 1
        return [-1]

s = Solution()
a = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
print(s.subArraySum(a, 42 , 468))