from collections import deque


def return_graph(matrix):
    m = len(matrix)
    n = len(matrix)
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(m)]
    cords = (
        (0, 1),
        (-1, 0),
        (1, 0),
        (0, -1),
    )

    q.append([(0, 0)])
    visited[0][0] = True
    max_route = float('-inf')
    while len(q) > 0:
        route = q.pop()
        c = route[-1]

        for cord in cords:
            x = c[0] + cord[0]
            y = c[1] + cord[1]
            if valid_cords(x, y, m, n, visited) and matrix[x][y] == 0:
                temp = route.copy()
                temp.append((x, y))
                visited[x][y] = True
                q.append(temp)
                if x == m-1 and y == n-1:
                    max_route = max(len(temp), max_route)

    print(max_route)


def valid_cords(x, y, m, n, visited):
    if 0 <= x < m and 0 <= y < n and visited[x][y] is False:
        return True
    return False


m, n = list(map(int, input().split()))
matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split())))
return_graph(matrix)


# 5 5
# 0 0 0 0 0
# 1 1 1 0 0
# 0 0 0 0 1
# 0 1 1 0 1
# 0 0 0 0 0


# 5 5
# 0 1 0 0 0
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 1 0 0
# 1 0 1 1 0
