#User function Template for python3


class Solution:

    #Function to sort the array according to frequency of elements.
    def sortByFreq(self, a, n):
        freq = []
        hash_table = dict()

        for i in a:
            count = hash_table.get(i, 0)
            count += 1
            hash_table[i] = count
        hash_new = {}
        for index, value in hash_table.items():
            elm = hash_new.get(value, [])
            elm.append(index)
            if len(elm) == 1:
                freq.append(value)
            else:
                elm.sort()

            hash_new[value] = elm

        freq.sort()
        freq.reverse()
        c = 0
        for i in freq:
            elm = hash_new.get(i)
            for j in elm:
                for _ in range(0, i):
                    a[c] = j
                    c += 1

        return a


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(a, n)
        print(*l)