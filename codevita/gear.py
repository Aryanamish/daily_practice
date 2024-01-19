from collections import deque
n = int(input())
gears = [list(map(int, input().split())) for _ in range(n)]

# n = 4
# gears = [
#     [1, 1, 1,],
#     [4, 1, 2,],
#     [1, 4, 1,],
#     [4, 4, 1,],
# ]


def solve(gears):
    graph = find_link(gears)
    path = shortest_path(graph)
    if path is False:
        return "Could Not Process"
    for p in path:
        if len(graph[p]) > 2:
            return "Could Not Process"
    for i in range(len(path) - 1):
        x1, y1, r1 = gears[path[i]]
        x2, y2, r2 = gears[path[i+1]]
        if dist(x1, y1, x2, y2) != r1 + r2:
            return "Could Not Process"
        else:
            next_turn = ()

    n1 = 1
    for i in range(len(path) - 1):
        x1, y1, r1 = gears[path[i]]
        x2, y2, r2 = gears[path[i + 1]]

        n2 = (n1 * r1) / r2
        n1 = n2
    return n1


def dist(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def find_link(gears):
    links = []

    graph = [[] for _ in range(len(gears))]

    for i in range(len(gears)):
        for j in range(i+1, len(gears)):
            x1, y1, r1 = gears[i]
            x2, y2, r2 = gears[j]
            if dist(x1, y1, x2, y2) == r1 + r2:
                graph[i].append(j)

    return graph


def shortest_path(graph):
    q = deque()
    cords = (
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1),
    )
    q.append([0])
    visited = [False] * len(graph)
    while len(q) > 0:
        node = q.popleft()
        visited[node[-1]] = True

        for n in graph[node[-1]]:
            if n == len(graph) - 1:
                return node + [n]
            if visited[n] is False:
                temp = node.copy()
                temp.append(n)
                q.append(temp)
    return False


print(solve(gears))

'''
4
1 1 1
4 1 2
1 4 1
4 4 1


5
4 9 2
7 9 1
9 9 1
7 7 1
6 4 1
'''
