def memoization(cache):
    def prefix(func):
        def wrapper(*args, **kwargs):
            lookup = ''
            for i in args:
                if i is not None:
                    lookup += str(i)
            
            for key,value in kwargs.items():
                lookup += str(key) + str(value)
            if lookup in cache:
                return cache[lookup]
            else:
                cache[lookup] = func(*args, **kwargs)
                return cache[lookup]
        return wrapper
    return prefix

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.bottom_up(s, p)

    def bottom_up(self, s, p):
        #Bottom Up
        p_len = len(p)
        s_len = len(s)
        dp = [[False for _ in range(s_len+1)] for _ in range(p_len+1)] 
        dp[0][0] = True
        if p[0] == '*':
            return False

        for i in range(1, p_len+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        match = lambda x, y: p[x-1] == s[y-1] or p[x-1] == '.'
        for i in range(1, p_len+1):
            for j in range(1, s_len+1):
                if match(i, j):
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    dp[i][j] = dp[i-2][j]
                    if match(i-1, j):
                        dp[i][j] = dp[i][j-1] or dp[i][j]
        return dp[p_len][s_len]


    def top_down(self, s, p):
        # top down
        @memoization(cache={})
        def dp(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                return dp(i, j+2) or (match and dp(i+1, j)) 

            if match:
                return dp(i+1, j+1)
            else:
                return False
        return dp(0,0)

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aaa', 'ab*a*c*a'))