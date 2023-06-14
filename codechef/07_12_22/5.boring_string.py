from random import randint

class BoringString:
    def __init__(self, string):
        self.length = len(string)
        self.string = string
        self.seen_string = {string[0]: 1}
    
    def increase_occur(self, string):
        if string == '':
            return 0
        occurance = self.seen_string.get(string, 0)
        occurance += 1
        self.seen_string[string] = occurance
        return occurance

    def count_all_boring_string(self):
        last_boring_string = self.string[0]
        for i in range(1, self.length):
            if self.string[i] == self.string[i - 1]:
                self.increase_occur(last_boring_string)
                last_boring_string += self.string[i]
            else:
                last_boring_string = self.string[i]
            
            self.increase_occur(last_boring_string)

    def get_longest_boring_string(self):
        self.count_all_boring_string()
        ans = 0      
        for key in self.seen_string:
            occurance = self.seen_string[key]
            if occurance > 1:
                ans = max(ans, len(key))
        return ans

t = int(input())
for i in range(t):
    n = randint(10**5, 2*10**5)
    string = ''
    j = 0
    while j < n:
        r = randint(1, n-j)
        string += chr(randint(97, 122)) * r
        j += r
    # n = int(input())
    # string = input()
    b_r = BoringString(string)
    b_r.get_longest_boring_string()
    # print(string)
    print(f"{i}: {b_r.get_longest_boring_string()}")