class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        x = str(abs(x))
        reversed_s = '' 
        for i in x:
            reversed_s = i + reversed_s
        reversed_s = int(reversed_s) if is_negative is False else int('-' + reversed_s)
        limit = -pow(2,31)
        if not(limit < reversed_s < abs(limit) - 1):
            return 0
        return reversed_s
    
    def reverse2(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = int('-' + x[:0:-1])
        else:
            x = int(x[::-1])

        if not(self.limit < x < abs(self.limit) - 1):
            return 0
        return x
        
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-2147483648))