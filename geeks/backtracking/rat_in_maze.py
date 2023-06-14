#User function Template for python3


#Function to find the minimum number of Hops required for the rat to
#reach from the source block to the destination block.
class Maze:

    def __init__(self, maze, n):
        self.maze = maze
        self.path = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.path[0][0] = 1

    def is_safe(self, cord):
        n = self.n
        if cord[0] == n - 1 and cord[1] == n - 1:
            return True
        if -1 < cord[0] < n and -1 < cord[1] < n and self.path[cord[0]][
                cord[1]] == 0:
            if self.maze[cord[0]][cord[1]] != 0:
                return True
        return False

    def solve(self, curr=[0, 0]):
        n = self.n
        if curr[0] == n - 1 and curr[1] == n - 1:
            return True

        maze = self.maze
        path = self.path
        hop = maze[curr[0]][curr[1]]
        possible_path = []
        for i in range(1, hop + 1):
            possible_path.append([curr[0], curr[1] + i])
            possible_path.append([curr[0] + i, curr[1]])
            possible_path.append([curr[0] - i, curr[1]])
            possible_path.append([curr[0], curr[1] - i])

        for cord in possible_path:
            if self.is_safe(cord):
                path[cord[0]][cord[1]] = 1
                if self.solve(cord):
                    return True
                path[cord[0]][cord[1]] = 0
        return False


def solve(N, maze):
    m = Maze(maze, N)
    if m.solve():
        for i in range(N):
            for j in range(N):
                print(m.path[i][j], end=" ")
            print()
    else:
        print("-1")


#{
# Driver Code Starts
#Initial Template for Python 3


def print_sol(n, sol):
    for i in range(n):
        for j in range(n):
            print(sol[i][j], end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        n = int(input())
        maze = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            maze[i] = [int(x) for x in input().strip().split()]
        solve(n, maze)
        t = t - 1
# } Driver Code Ends