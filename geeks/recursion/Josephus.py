#{ 
#Driver Code Starts
import math



 # } Driver Code Ends
#Complete this function

class Solution:
    def josephus(self,n,k):
        remove = []
        circle = [i for i in range(1, n+1)]

        def recursion(p, left):
            if p-1 >= left:
                p = p-left
            if left == 1:
                return circle.pop()
            remove.append(p-1)
            circle[p-1] = 0
            
            return recursion(p+k, left-1)
        return recursion(k, n)
        
#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(Solution().josephus(n,k))
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends