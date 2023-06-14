#User function Template for python3


class Solution:

    #Function to check if two strings are isomorphic.
    def areIsomorphic(self, str1, str2):
        if len(str1) != len(str2):
            return False
        str1_map = {}
        hash_val1 = 0
        count = 1
        for i in str1:
            c = str1_map.get(i)
            if c is None:
                c = count
                count += 1
                str1_map[i] = c

            hash_val1 += c

        str2_map = {}
        hash_val2 = 0
        count = 1
        for i in str2:
            c = str2_map.get(i)
            if c is None:
                c = count
                count += 1
                str2_map[i] = c

            hash_val2 += c

        return hash_val1 == hash_val2


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        ob = Solution()
        if (ob.areIsomorphic(s, p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends