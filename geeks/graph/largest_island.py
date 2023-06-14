from collections import deque


class Solution:

    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans = max(ans, self.BFS(grid, i, j))
        return ans

    def BFS(self, grid, i, j):
        q = deque()

        quardinates = (
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, -1),
        )
        q.append((i, j))
        grid[i][j] = 0
        count = 0
        m = len(grid)
        n = len(grid[i])
        while len(q) != 0:
            temp = q.popleft()
            count += 1
            for quad in quardinates:
                x = quad[0] + temp[0]
                y = quad[1] + temp[1]

                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 0
                    q.append((x, y))
        return count


#{
# Driver Code Starts

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends