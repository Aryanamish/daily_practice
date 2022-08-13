#User function Template for python3

keys = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}
class Solution:
    
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        # a = [2,3,4]
        rv_list = []
        def recursion(arr, string):
            if len(arr) == 1:
                for i in keys[arr[0]]:
                    rv_list.append(string+i)
                        
                return ''
            
            for i in arr:
                for j in keys[i]:
                    recursion(arr[1:], string+j)
            return ''
        recursion(a, '')
        return rv_list
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends