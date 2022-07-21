#{ 
#Driver Code Starts
#Initial Template for Python 3

import math




    
 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        if m == n:
            return -1
        m, n = max(m,n), min(m,n)
        m = bin(m)[2:]
        n = bin(n)[2:]
        
        n = '0'*(len(m) - len(n)) + n
        
        for i in range(1, min(len(m), len(n)) + 1):
            if m[-i] != n[-i]:
                return i
        return min(len(m), len(n)) + 1

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends