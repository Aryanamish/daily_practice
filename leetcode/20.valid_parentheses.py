
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = {
            '(': 1,
            '[': 2,
            '{': 3,
        }
        close_bracket = {
            ')': 1,
            ']': 2,
            '}': 3,
        }

        for i in s:
            if i in open_brackets:
                stack.append(open_brackets[i])
            elif i in close_bracket and len(stack) > 0:
                if stack.pop() == close_bracket[i]:
                    continue
                else:
                    return False
            else:
                return False
        return len(stack) == 0
            

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('('))