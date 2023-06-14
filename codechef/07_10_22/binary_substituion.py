# cook your dish here
class Solution:
    patt = {'ab', 'ba'}
    def __init__(self, string):
        self.str = string
        self.count = 0
        self.dp = {}
        self.length = len(string)
    
    def possible_values(self, index, max_length):
        ans = self.dp.get(index, None)
        if ans is not None:
            return ans
        if index >= max_length:
            return 1
        x = self.possible_values(index+1, max_length)
        if index + 1 < max_length:
            if self.str[index] + self.str[index+1] in self.patt:
                x += self.possible_values(index+2, max_length)
        self.dp[index] = x
        
        return x

    def solve(self):
        max_depth = min(100, self.length)
        ans = self.possible_values(0, max_depth)
        max_depth += 100
        max_depth = min(max_depth, self.length)

        while max_depth <= self.length:
            self.dp = {}
            ans += self.possible_values(max_depth-99, max_depth)
            if max_depth == self.length:
                break
            max_depth += 100
            max_depth = min(max_depth, self.length)

        return ans % 998244353
# 265214231

# for _ in range(int(input())):
#     s = Solution(input())
#     print(s.solve())


n=int(input())
for op in range(n):
    st=input()
    li = [0]*(len(st)+1)
    li[-1],li[-2] = 1,1
    for k in range ( len(st)-2 , -1 ,-1 ):
        if( st[k]== st[k+1] ):
            li[k] = li[k+1]
        else:
            li[k] = (li[k+1] + li[k+2])
    print(li[0]% 998244353)
    
    




mod = 998244353

# T = int(input())
# for _ in range(T):
#     # N=int(input())
#     # N,M=map(int,input().split())
#     # A=list(map(int,input().split()))
#     B = input()
#     L_B = len(B)

#     A = [0]*(L_B+1)
#     A[-1], A[-2] = 1, 1
#     for i in range(L_B - 2, -1, -1):
#         if B[i] == B[i + 1]: 
#             A[i] = A[i + 1]
#         else:
#             A[i] = (A[i + 1] + A[i + 2]) % mod
#     print(A[0] % mod)