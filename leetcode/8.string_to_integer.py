class Solution:
    limit = -pow(2,31)
    allowed = {str(i) for i in range(0,10)}

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] not in self.allowed and s[0] != '-' and s[0] != '+':
            return 0
        negative = True if s[0] == '-' else False
        number = ''
        for i in range(len(s)):
            if s[i] in self.allowed:
                number += s[i]
            else:
                if i == 0  and (s[i] == '-' or s[i] == "+"):
                    continue
                else:
                    break
        if number != '':
            number = int('-'+ number) if negative is True else int(number)
        else:
            number = 0
        return max(self.limit, number) if number < 0 else min(abs(self.limit), number)

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("+1"))