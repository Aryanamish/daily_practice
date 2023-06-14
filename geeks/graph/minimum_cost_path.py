from queue import PriorityQueue


class Solution:

    #Function to return the minimum cost to react at bottom
    #right cell from top left cell.
    def minimumCostPath(self, grid):

        def recursion(grid):
            pq = PriorityQueue()
            pq.put((grid[0][0], [(0, 0)]))
            m = len(grid)
            n = len(grid[0])
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[0][0] = True
            coordinates = ((0, 1), (0, -1), (1, 0), (-1, 0))

            while pq.empty() is False:
                u = pq.get()
                result = u[0]
                quad = u[1][-1]
                for q in coordinates:
                    x = quad[0] + q[0]
                    y = quad[1] + q[1]
                    if x == m - 1 and y == n - 1:
                        result += grid[x][y]
                        return [result, u[1]]
                    if 0 <= x < m and 0 <= y < n and visited[x][y] is False:
                        visited[x][y] = True
                        asd = u[1].copy()
                        asd.append((x, y))
                        pq.put((result + grid[x][y], asd))
            return u

        ans = recursion(grid)
        for i in ans[1]:
            grid[i[0]][i[1]] = [grid[i[0]][i[1]]]
        return ans[0]


'''
4
9 4 9 9 
6 7 6 4 
8 3 3 7 
7 4 1 10 
'''
#{
# Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.minimumCostPath(grid)
        print(ans)

# } Driver Code Ends
'''
9
2   9   6   6   6   2   10  1   9
7   10  10  8   3   3   4   7   9
9   9   9   8   6   2   5   7   2
7   9   3   10  10  8   6   6   10
8   9   9   6   9   5   10  6   10
10  5   9   3   9   10  1   8   4
9   8   9   2   5   3   5   4   5
5   3   2   5   1   1   5   2   4
7   9   6   1   9   9   2   7   2
'''
''''''