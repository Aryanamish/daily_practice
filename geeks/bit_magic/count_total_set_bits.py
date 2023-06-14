#User function Template for python3
set_bits = [[0, 0]]

for i in range(1, 256):
    sb = (i & 1) + set_bits[i // 2][0]
    set_bits.append([sb, sb + set_bits[i - 1][1]])


class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self, n):
        count = 1
        while n > 0:
            count += set_bits[n & 255][1]
            n = n >> 8
        return count


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        ob = Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends
'''
00001 = 1
00010 = 2
00011 = 3
00100 = 4
00101 = 5
00110 = 6                   p*pow(2, p)/2 + solve(n - pow(2,p)) + (n - pow(2,p)+1)
00111 = 7
01000 = 8
01001 = 9
01010 = 10
01011 = 11
01100 = 12
01101 = 13
01110 = 14
01111 = 15
10000 = 16
10001 = 17
10010 = 18
10011 = 19
10100 = 20
10101 = 21
10110 = 22
10111 = 23
11000 = 24
11001 = 25
11010 = 26
11011 = 27
11100 = 28
11101 = 29
11110 = 30
11111 = 31
'''