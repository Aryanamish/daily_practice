class Solution:
    def correct_password(self, passwords):
        found = set()
        for p in passwords:
            p_ = list(p)
            p_.reverse()
            p_ = "".join(p_)
            if p_ in found:
                return p
            found.add(p_)
        
        
passwords = [
    "ajephhgpogqws",
    "jqukotrwwhuqe",
    "jhrmnvvbaephh",
    "jxxpfbyjqisyx",
    "hhpeabvvnmrhj",
    ]

s = Solution()
a = s.correct_password(passwords)
print(a)