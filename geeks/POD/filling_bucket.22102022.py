#User function Template for python3


class Solution:
    MOD = 10**8

    def facto_0(self, x):
        if x == 0 or x == 1:
            return 1
        else:
            return x

    def fill_the_bucket(self, n):
        twos = 0
        ones = n
        ans = 1
        numerator = ones
        denominator1 = ones
        denominator2 = twos
        fraction = f"{numerator}!/{denominator1}! {denominator2}!"
        prev_fact = 1
        while ones > 1:
            fact = int((prev_fact * self.facto_0(denominator1) *
                        self.facto_0(denominator1 - 1) *
                        (1 / self.facto_0(numerator)) *
                        (1 / self.facto_0(denominator2 + 1))) % self.MOD)
            numerator -= 1
            denominator1 -= 2
            denominator2 += 1
            fraction = f"{numerator}!/{denominator1}! {denominator2}!"
            ans = (ans + int(fact)) % self.MOD
            prev_fact = int(fact)
            twos += 1
            ones -= 2
        return ans

    def fillingBucket(self, N):
        ans = self.fill_the_bucket(N)
        return ans


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.fillingBucket(N))
# } Driver Code Ends