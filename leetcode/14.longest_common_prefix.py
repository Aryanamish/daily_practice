class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            strs = sorted(strs, key=lambda x:len(x))
            string = strs[0]
            i = 1
            while len(string) > 0 and i < len(strs):
                if strs[i].startswith(string):
                    i+=1
                else:
                    string = string[:-1]

        return string


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))