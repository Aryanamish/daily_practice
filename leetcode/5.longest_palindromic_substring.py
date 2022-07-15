import parent
from datastructure.timer import performance

class Solution:
    palindrome = {}
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start = 0
        end = 0
        
        for i in range(length):
            len1 = self.centerSpreadPalindrome(s, i, i+1)
            len2 = self.centerSpreadPalindrome(s, i, i)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = max(i - (max_len//2) - 1,0)
                end = min(i + max_len//2, length)
        return s[start:end]
        
    def centerSpreadPalindrome(self, s, left, right):
        while left <= right and right < len(s) and left >= 0 and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
            

if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome("ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy")