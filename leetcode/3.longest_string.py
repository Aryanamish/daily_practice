class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        longest_string_len = 0
        length = len(s)
        for i in range(length):
            longest_string = {s[i]:True, 'length': 1}
            for j in range(i + 1, length):
                if s[j] in longest_string:
                    break
                else:
                    longest_string[s[j]] = True
                    longest_string['length'] += 1
            if longest_string['length'] > longest_string_len:
                longest_string_len = longest_string['length']

        return longest_string_len

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))