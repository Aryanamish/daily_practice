#User function Template for python3


class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self, arr, n):

        seen = {}
        repeated = set()
        for i in range(n):
            if seen.get(arr[i]) is None:
                seen[arr[i]] = i
            else:
                repeated.add(seen[arr[i]])

        minimun_index = float('inf')
        for index in repeated:
            minimun_index = min(minimun_index, index)

        return minimun_index + 1 if minimun_index in repeated else -1


#{
# Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends