#User function Template for python3


class Solution:

    #Function to print all words in the CamelCase dictionary
    #that matches with a given pattern.
    def __init__(self):
        self.data = {}

    def findAllWords(self, d, pattern):
        data = {}
        for string in d:
            code = ''
            for char in string:
                if char.isupper() is True:
                    code += char
            l = data.get(char, [])
            l.append(string)
            data[code] = l

        d = data.get(pattern, None)
        if d is None:
            print("No match found")
        else:
            for i in d:
                print(i)


#{
# Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = input().strip().split()
        pattern = input()
        Solution().findAllWords(arr, pattern)
        print()
# } Driver Code Ends