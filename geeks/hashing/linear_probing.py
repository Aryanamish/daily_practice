#User function Template for python3

from operator import truediv


class Solution:
    #Function to fill the array elements into a hash table
    #using Linear Probing to handle collisions.
    def linearProbing(self, hashSize, arr, sizeOfArray):
        hash = [-1] * hashSize
        full_signal = False
        for i in arr:
            if full_signal is True:
                hash[i % hashSize] = i
            index = (i % hashSize)
            start_index = index
            while full_signal is False:
                if hash[index] == -1 or hash[index] == i:
                    hash[index] = i
                    break
                else:
                    index += 1
                    if index >= len(hash):
                        index = 0
                if index == start_index:
                    full_signal = True

        return hash


#{
# Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):

        hashSize = int(input())
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        hash = obj.linearProbing(hashSize, arr, sizeOfArray)

        for i in hash:
            print(i, end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends