#User function Template for python3


class Solution:
    #Function to check if two arrays are equal or not.
    def check(self, A, B, N):

        found = dict()
        for i in A:
            count = found.get(i, 0)
            count += 1
            found[i] = count

        for j in B:
            count = found.get(j)
            if count is None:
                return False
            count -= 1
            if count == 0:
                del found[j]
            else:
                found[j] = count
        return True if len(found) == 0 else False


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):

        N = int(input())

        A = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.check(A, B, N):
            print(1)
        else:
            print(0)

# } Driver Code Ends