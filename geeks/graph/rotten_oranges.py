from collections import deque


class Solution:

    #Function to find minimum time required to rot all oranges.
    def orangesRotting(self, grid):
        q = deque()
        nice_oranges = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                q_str = str(i) + ", " + str(j)
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    nice_oranges.add(q_str)
        while len(q) != 0 and len(nice_oranges) != 0:
            count += 1
            q = self.rot_orange(grid, q, nice_oranges)
        if len(nice_oranges) == 0:
            return count
        else:
            return -1

    def rot_orange(self, grid, q, nice_oranges):
        quardinates = ((0, 1), (0, -1), (-1, 0), (1, 0))
        new_q = deque()
        m = len(grid)
        n = len(grid[0])
        while len(q) != 0:
            temp = q.popleft()
            for quad in quardinates:
                x = temp[0] + quad[0]
                y = temp[1] + quad[1]
                orange_str = str(x) + ', ' + str(y)
                if 0 <= x < m and 0 <= y < n and orange_str in nice_oranges:
                    grid[x][y] = 2
                    nice_oranges.remove(orange_str)
                    new_q.append((x, y))
        return new_q


#{
# Driver Code Starts
from queue import Queue

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.orangesRotting(grid)
        print(ans)

# } Driver Code Ends