#User function Template for python3
from queue import PriorityQueue


class Solution:
    #Function to return kth largest element from an array.
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify(self, arr, size, i=0):
        while True:
            small = i
            left = self.left(i)
            right = self.right(i)

            if left < size and arr[left] < arr[small]:
                small = left

            if right < size and arr[right] < arr[small]:
                small = right

            if small != i:
                arr[i], arr[small] = arr[small], arr[i]
                i = small
            else:
                break

    def build_heap(self, arr, n):
        parent = self.parent(n - 1)
        for i in range(parent, -1, -1):
            self.heapify(arr, n, i)

    def kthLargest(self, arr, n, k):
        q = PriorityQueue()

        for i in range(k):
            q.put(i)

        for i in range(k, n):
            if arr[i] > q.queue[0]:
                q.get()
                q.put(arr[i])

        return q.get()


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.kthLargest(a, n, k))
# } Driver Code Ends