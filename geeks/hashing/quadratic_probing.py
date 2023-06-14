#User function Template for python3
class Solution:

    #Function to fill the array elements into a hash table
    #using Quadratic Probing to handle collisions.
    def QuadraticProbing(self, hash, hashSize, arr, N):

        hash_table_filled = 0
        for i in arr:
            index = i % hashSize
            count = 1
            while hash_table_filled < hashSize:
                if hash[index] == -1 or hash[index] == i:
                    if hash[index] != i:
                        hash_table_filled += 1
                        hash[index] = i
                    break
                else:
                    index = (i + count * count) % hashSize
                    count += 1


#{
# Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):

        hashSize = int(input())
        N = int(input())
        arr = [int(x) for x in input().strip().split()]

        hash = [-1] * hashSize
        obj = Solution()
        obj.QuadraticProbing(hash, hashSize, arr, N)

        for i in hash:
            print(i, end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends