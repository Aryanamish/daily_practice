class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        sum_n = sum_sq_n = sum_actual = sum_sq_actual = 0
        for i in range(1, len(A)+1):
            sum_n += i
            sum_sq_n += i * i
            sum_actual += A[i-1]
            sum_sq_actual += A[i-1] * A[i-1]

        m_minus_r = sum_n - sum_actual
        m_sq_minus_r_sq = sum_sq_n - sum_sq_actual

        m_plus_r = m_sq_minus_r_sq // m_minus_r

        R = (m_plus_r - m_minus_r)//2
        M = (m_minus_r + m_plus_r)//2

        return [R, M]


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedNumber([3, 1, 2, 5, 3]))
