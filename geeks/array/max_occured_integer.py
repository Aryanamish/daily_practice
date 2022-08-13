#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,L,R,N,maxx):
        ranges = [[L[0], R[0]]]
        max_occur = dict()
        
        def inc(n):
            if max_occur.get(n) is None:
                max_occur[n] = 1
            else:
                max_occur[n] += 1
        
        for i in range(1, N):
            cur_r = [L[i], R[i]]
            for j in ranges:
                cur_r = max(cur_r, j)
                j = min(cur_r, j)
                if cur_r[1] > j[0]:
                    inc(j[0])
                    inc(j[1])

                    continue
                inc(max(cur_r[0], j[0]))
                inc(min(cur_r[1], j[1]))
            ranges.append(cur_r)
        ans = [0, 0]
        for i in max_occur:
            if ans[1] < max_occur[i]:
                ans[1] = max_occur[i]
                ans[0] = i
                
        return ans[0]
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math

A=[0]*1000000


            

def main():
    
    T=int(input())
    
    while(T>0):
        
        global A
        A=[0]*1000000
        
        N=int(input())
        
        L=[int(x) for x in input().strip().split()]
        R=[int(x) for x in input().strip().split()]
        
        maxx=max(R)
        ob=Solution()
        print(ob.maxOccured(L,R,N,maxx))
            
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends