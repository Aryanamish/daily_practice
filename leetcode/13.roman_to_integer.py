class Solution:
    def romanToInt(self, s: str) -> int:
        d = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I']
        ]
        num = 0
        for i in d:
            if s.startswith(i[1]):
                for _  in '123':
                    if s.startswith(i[1]):
                        s = s[1:] if len(i[1]) == 1 else s[2:]
                        num +=  i[0]
                    else:
                        break          
        print(num)

if __name__ == '__main__':
    s = Solution()
    s.romanToInt('MMMCMXCIX')