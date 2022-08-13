#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        new_arr = A[:D]
        new_arr.reverse()
        i = 0
        j = D
        
        while i < N:
            A[i], A[j] = A[j], A[i]
            x = A[:i+1]

            i += 1
            if j + 1 == N or j == -1:
                j = -1
            else:
                j += 1
            
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends