#User function Template for python3
set_bits = [0]

for i in range(1, 256):
    set_bits.append(i&1 + (set_bits[i//2]))

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        count = 0
        for i in range(1, 5):
            while i > 0:
                count += set_bits[i & 0x76]
                i = i >> 8
        return count
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends