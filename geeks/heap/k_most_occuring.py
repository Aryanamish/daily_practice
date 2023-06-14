#User function Template for python3


class PriorityQueue:

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return self.__str__()

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return (2 * i) + 1

    def right(self, i):
        return (2 * i) + 2

    def __init__(self):
        self.heap = []
        self.key = {}

    def heapify(self, i):
        if i < 0:
            return
        left = self.left(i)
        right = self.right(i)
        small = i
        arr = self.heap
        if left < len(arr) and arr[left][0] > arr[small][0]:
            small = left
        if right < len(arr) and arr[right][0] > arr[small][0]:
            small = right

        if small != i:
            self.key[arr[small][1]] = i
            self.key[arr[i][1]] = small
            arr[small], arr[i] = arr[i], arr[small]
            self.heapify(small)

    def put(self, key):
        arr = self.heap
        prev_val = self.key.get(key, None)
        if prev_val is None:
            arr.append([1, key])
            self.key[key] = len(arr) - 1
            self.heapify(self.parent(len(arr) - 1))
        else:
            arr[prev_val][0] += 1
            self.heapify(self.parent(prev_val))

    def get(self):
        arr = self.heap
        arr[0], arr[-1] = arr[-1], arr[0]
        self.key[arr[0][1]] = 0
        val = arr.pop()
        self.heapify(0)
        del self.key[val[1]]
        return val[0]


class Solution:

    #Function to return the sum of frequencies of k numbers
    #with most occurrences in an array.
    def kMostFrequent(self, arr, n, k):
        pq = PriorityQueue()
        for i in arr:
            pq.put(i)
        ans = 0
        for _ in range(k):
            ans += pq.get()
        return ans


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kMostFrequent(a, n, k))
# } Driver Code Ends