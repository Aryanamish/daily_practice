import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        s = re.sub(r"[^a-z0-9]", "", s.lower())
        new_s = list(s)
        new_s.reverse()
        return s == "".join(new_s)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))