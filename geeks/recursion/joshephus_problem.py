#{
#Driver Code Starts
import math

# } Driver Code Ends
#Complete this function


class Solution:

    def solve(self, n, k, circle, remove_index):
        if n == 1:
            for i in range(len(circle)):
                if circle[i] == 1:
                    return i + 1
        circle[remove_index - 1] = 0
        remove_index += k
        if remove_index >= len(circle):
            remove_index -= len(circle)
        return self.solve(n - 1, k, circle, remove_index)

    def josephus(self, n, k):
        ans = self.solve(n, k, [i for i in range(n)], k)
        return ans


#{
#Driver Code Starts.


def main():

    T = int(input())

    while (T > 0):

        nk = [int(x) for x in input().strip().split()]
        n = nk[0]
        k = nk[1]

        print(Solution().josephus(n, k))

        T -= 1


if __name__ == "__main__":
    main()
#} Driver Code Ends