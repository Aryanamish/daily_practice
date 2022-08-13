#User function Template for python3

class Solution:
    #Complete this function
    #Function to find minimum adjacent difference in a circular array.
    def minAdjDiff(self,arr, n):
        ans = abs(arr[-1] - arr[0])
        
        for i in range(0, n-1):
            ans = min(ans, abs(arr[i] - arr[i+1]))
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
       
        ob=Solution()
        print(ob.minAdjDiff(arr,n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends