#User function Template for python3
class TwoArray:

    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        self.n = len(arr1)
        self.m = len(arr2)
        self.length = len(arr1) + len(arr2)

    def __getitem__(self, index):
        if index < self.n:
            return self.arr1[index]
        else:
            return self.arr2[index - self.n]

    def __setitem__(self, index, value):
        if index < self.n:
            self.arr1[index] = value
        else:
            self.arr2[index - self.n] = value

    def __len__(self):
        return len(self.arr1) + len(self.arr2)

    def __str__(self):
        return str([i for i in self.arr1] + [j for j in self.arr2])

    def __repr__(self) -> str:
        return self.__str__()


class Solution:

    #Function to merge the arrays.
    def mergeArr(self, arr, low, high):
        mid = (low + high) // 2
        left = [arr[i] for i in range(low, mid)]
        right = [arr[i] for i in range(mid, high)]
        i = j = 0
        k = low

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, low, high):
        if low < high:
            mid = low + (high - low) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)
            self.mergeArr(arr, low, high)

    def merge(self, arr1, arr2, n, m):
        arr = TwoArray(arr1, arr2)
        self.mergeSort(arr, 0, len(arr))


#{
# Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n, m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1, end=" ")
        print(*arr2)
# } Driver Code Ends