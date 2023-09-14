class Solution:
    # @param A : list of integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        seen_xor = set([0])
        xor = A[0]
        count = 0 if A[0] != B else 1
        for n in A[1:]:
            xor ^= n
            if n == B:
                count += 1
            if xor ^ B in seen_xor:
                count += 1
            seen_xor.add(xor)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.solve([5, 6, 7, 8, 9], 5))
