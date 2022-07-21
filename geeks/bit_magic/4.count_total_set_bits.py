#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    two_power = {2**i: i for i in range(0,27)}
    def countSetBits(self,n):
        two_power = 0
        for i in self.two_power:
            if n == i:
                two_power = self.two_power[i] 
                break
            if n < i:
                two_power = self.two_power[i] - 1
                break
        count  = 0
        while two_power >= 0:
            count += 2**two_power
            two_power -= 1
        
        return count
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends