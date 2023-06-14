#code
def dfs(graph, target, weight, node, visited):
    if node == target:
        return weight
    if visited[node] is True:
        return False
    visited[node] = True
    min_w = weight
    for edge in graph[node]:
        if visited[edge[0]] is False:
            ans = dfs(graph, target, weight + edge[1], edge[0], visited)
            if ans:
                min_w = min(min_w, ans)
    return min_w


t = int(input())
for _ in range(t):
    v, e = list(map(int, input().split()))
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        u, v, w = list(map(int, input().split()))
        graph[u].append([v, w])
        graph[v].append([u, w])
    source, k = list(map(int, input().split()))
    flags = list(map(int, input().split()))
    ans = 0
    for flag in flags:
        w = float('inf')
        for node in graph[source]:
            visited = [False] * (v + 1)
            if visited[node[0]] == False:
                w = min(w, dfs(graph, flag, node[1], node[0], visited))
        ans += 2 * w
        print(w, ' for ', flag)

    print(ans)
