class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p[0] == '*':
            return False
        if p == '.*':
            return True
        string_pointer = 0
        s_len = len(s)
        match_found = False
        for i in range(len(p)):
            wild_card = True if p[i] == '*' else False
            char = p[i] if wild_card is False else p[i-1]
            next_char = p[i+1] if i+1 < len(p) else None

            for j in range(string_pointer, len(s)):

                if char == '.':
                    string_pointer = j+1
                    if wild_card is True:
                        continue
                    break
                

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aba', '.*'))                   # True
    print(s.isMatch('aa', 'a'))                     # False
    print(s.isMatch('aa', 'a*'))                    # True
    print(s.isMatch('ab', '.*'))                    # True
    print(s.isMatch('aab', 'c*a*b'))                # True
    print(s.isMatch('mississippi', 'mis*is*ip*.'))  # True
    print(s.isMatch('mississippi', 'mis*is*p*.'))   # False
    print(s.isMatch('ab', '.*c'))                   # False
    print(s.isMatch('aaa', 'a*a'))                  # True
    print(s.isMatch('aab', 'c*a*b'))                # True

