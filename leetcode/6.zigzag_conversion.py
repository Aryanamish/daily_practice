class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        final_string_list = ['' for i in range(numRows)]
        count = 0
        reverse = False
        for i in s:
            final_string_list[count] += i
            if reverse is False:
                if count < numRows-1:
                    count += 1
                else:
                    reverse = True
                    count -= 1
            else:
                if count != 0:
                    count -= 1
                else:
                    count += 1
                    reverse = False
        return ''.join(final_string_list)
            
            
            

if __name__ == '__main__':
    s = Solution()
    print(s.convert("ABC", 2))