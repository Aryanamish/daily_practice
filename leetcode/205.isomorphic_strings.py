class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        new = [s, t]
        count = 0
        for i in s:
            if i not in mapping:
                new[0] = new[0].replace(i, )
                
            count += 1

if __name__ == '__main__':
    s = Solution()
    # print(s.isIsomorphic("badc","baba"))
    print(s.isIsomorphic("paper","title"))