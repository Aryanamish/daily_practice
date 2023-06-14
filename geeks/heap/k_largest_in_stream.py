#User function Template for python3
import heapq


class Solution:
    #Function to print kth largest element for each element in the stream.
    def kthLargest(self, arr, n, k):
        heap = arr[:k]
        heapq.heapify(heap)

        print("-1 " * (k - 1), end="")
        for i in range(k, n):
            print(heap[0], end=" ")
            if arr[i] > heap[0]:
                heapq.heapreplace(heap, arr[i])
        print(heap[0], end=" ")


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k, n = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ob.kthLargest(a, n, k)
        print()

# } Driver Code Ends