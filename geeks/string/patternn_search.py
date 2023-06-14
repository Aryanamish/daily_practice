class Solution:

    def check_(self, patt, txt, idx):
        for i in range(0, len(patt)):
            if txt[i + idx] != patt[i]:
                return False
        return True

    def search(self, patt, txt):

        def ctt(char):
            return ord(char) - 96

        m = len(patt)
        n = len(txt)
        patt_hash = 0
        txt_hash = 0

        d = 26
        q = 5381
        h = pow(d, m - 1)
        for i in range(0, m):
            patt_hash += (ctt(patt[i]) * pow(d, (m - i - 1)))
            txt_hash += (ctt(txt[i]) * pow(d, (m - i - 1)))

        for i in range(0, n - m + 1):
            if txt_hash == patt_hash and self.check_(patt, txt, i) is True:
                return True
            if i < n - m:
                txt_hash = (d * (txt_hash - ctt(txt[i]) * h) + ctt(txt[i + m]))
        return False


if __name__ == '__main__':

    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        obj = Solution()
        if (obj.search(p, s)):
            print("Yes")
        else:
            print("No")