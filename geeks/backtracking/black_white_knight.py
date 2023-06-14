#User function Template for python3


#Function to find out the number of ways we can place a black and a white
#Knight on this chessboard such that they cannot attack each other.
class ChessBoard:

    def __init__(self, m, n):
        self.board = [[0 for _ in range(m)] for _ in range(n)]
        self.dim = (m, n)
        self.count = 0
        self.total_slots = m * n

    def is_safe(self, pos):
        if -1 < pos[0] < m and -1 < pos[1] < n:
            return pos

    def count_pos(self, k1):
        atack_pos = [
            self.is_safe((k1[0] + 2, k1[1] + 1)),
            self.is_safe((k1[0] + 2, k1[1] - 1)),
            self.is_safe((k1[0] - 2, k1[1] + 1)),
            self.is_safe((k1[0] - 2, k1[1] - 1)),
            self.is_safe((k1[0] + 1, k1[1] + 2)),
            self.is_safe((k1[0] - 1, k1[1] + 2)),
            self.is_safe((k1[0] + 1, k1[1] - 2)),
            self.is_safe((k1[0] - 1, k1[1] - 2)),
        ]
        atack_count = 0
        for i in atack_pos:
            if i is not None:
                atack_count += 1
        self.count += self.total_slots - atack_count - 1

    def solve(self, k1=(0, 0)):
        for i in range(m):
            for j in range(n):
                self.count_pos((i, j))


def numOfWays(M, N):
    chess = ChessBoard(M, N)
    chess.solve()
    return chess.count


#{
# Driver Code Starts
#Initial Template for Python 3
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m, n = map(int, input().strip().split())
        print(numOfWays(m, n))

# } Driver Code Ends