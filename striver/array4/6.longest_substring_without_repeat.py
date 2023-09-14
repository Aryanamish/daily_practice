class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        last_loc = {}
        ans = 1
        start_pos = 0
        for i in range(n):
            if s[i] in last_loc:
                start_pos = max(start_pos, last_loc[s[i]])
            last_loc[s[i]] = i + 1

            ans = max(ans, i - start_pos + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abba'))
