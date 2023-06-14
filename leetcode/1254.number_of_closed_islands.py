from collections import deque

cords = [
    [1,0],
    [-1,0],
    [0,1],
    [0,-1],
]
class Solution:

    def check_cords(self, x, y, m, n):
        if x >= 0 and x < m and y >= 0 and y < n:
            return True
        return False

    def check_close_island(self, grid, i, j, visited):
        m = len(grid)
        n = len(grid[0])
        q = deque()
        q.append((i, j))
        island = 1
        while len(q) > 0:
            pos = q.popleft()
            visited[pos[0]][pos[1]] = 1
            for cord in cords:
                x = cord[0] + pos[0]
                y = cord[1] + pos[1]
                if self.check_cords(x, y, m, n):
                    if grid[x][y] == 0 and visited[x][y] == 0:
                        q.append((x, y))
                else:
                    island = 0
        return island




    def closedIsland(self, grid):
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and visited[i][j] == 0:
                    island += self.check_close_island(grid, i, j, visited)
        return island
                    

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
if __name__ == '__main__':
    s = Solution()
    print(s.closedIsland(grid))



