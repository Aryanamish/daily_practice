#User function Template for python3
class Solution:
    #Complete this function
    # Function for finding maximum AND value.

    def maxAND(self, arr,N):
        max_length = 0
        for i in range(N):
            arr[i] = bin(arr[i])[2:]
            max_length = max(max_length, len(arr[i]))
        
        max_numebr = ['0' for i in range(max_length)]
        length = 0
        for i in range(max_length-1, -1, -1):
            found = False
            for j in arr:
                if len(j) > i:
                    continue
                if j[i] == 1:
                    if found is False:
                        found = True
                    else:
                        if len(j) >= length:
                            max_number[i] = '1'
                            length = len(j)
                        break
        return int("".join(max_number), 2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxAND(arr,n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends