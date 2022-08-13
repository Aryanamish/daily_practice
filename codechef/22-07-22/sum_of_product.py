SIZE = 100_001  # factorial size will be 300_003
factorial, MOD = [1] * (3 * SIZE), 998_244_353

# gfg algo for creating an array of factorial

# calculating 3 factoreial at a same time to minimize the loop
for i in range(2, SIZE):
    # between 1 to 100_001
    factorial[i] = factorial[i - 1] * i % MOD

    # between 100_001 to 200_002
    factorial[i + SIZE] = MOD - MOD // i * factorial[MOD % i + SIZE] % MOD
    
    # between 200_002 to 300_003
    factorial[i + (2 * SIZE)] = factorial[i - 1 + (2 * SIZE)] * factorial[i + SIZE] % MOD
            
class Solution:


    def get_mod(self, x,y):
        return factorial[x] * factorial[y + (2 * SIZE)] * factorial[x - y + (2 * SIZE)] % MOD

    def sum_of_product_2(self, n, arr):
        zero_appears = arr.count(0)
        t = 0
        for i in range(n - zero_appears + 1):
            if not (n - i < 0 or zero_appears > n - i):
                t += i * self.get_mod(n - i, zero_appears) % MOD
        return (t * (zero_appears + 1) * factorial[n - zero_appears] * factorial[zero_appears] % MOD)

for tc in range(int(input())):
    s = Solution()
    print(s.sum_of_product_2(int(input()), tuple(map(int, input().split()))))
    