class Solution:
    #Function to return k largest elements from an array.
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

            if left < size and arr[left] > arr[small]:
                small = left

            if right < size and arr[right] > arr[small]:
                small = right

            if small != i:
                arr[i], arr[small] = arr[small], arr[i]
                i = small
            else:
                break

    def extractMax(self, arr, size):

        if size[0] == 0:
            return -1
        elif size[0] == 1:
            size[0] -= 1
            return arr[0]
        if size[0] > 0:
            size[0] -= 1
            result = arr[0]
            arr[0] = arr[size[0]]
            arr[size[0]] = 0
            self.heapify(arr, size[0], 0)
            return result

    def build_heap(self, arr, n):
        parent = self.parent(n - 1)
        for i in range(parent, -1, -1):
            self.heapify(arr, n, i)

    def kLargest(self, arr, n, k):
        size = [n]
        ans = []
        for i in range(k):
            ans.append(self.extractMax(arr, size))
        return ans


h = Solution()
arr = [12, 5, 787, 1, 23]
h.build_heap(arr, len(arr))
print(arr)
size = [len(arr)]
print(h.extractMax(arr, size))
print(h.extractMax(arr, size))