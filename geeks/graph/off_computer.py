from collections import deque


def solve(systemState, dist):
    n = len(systemState)
    q = deque()
    for i in range(len(systemState)):
        if systemState[i] == 1:
            q.append(i)
    ans = 0
    while len(q) != 0:
        x = q.popleft()
        if x - 1 >= 0 and systemState[x - 1] == 0:
            systemState[x - 1] = 1
            ans += abs(dist[x] - dist[x - 1])
            q.append(x - 1)
        if x + 1 < n and systemState[x + 1] == 0:
            systemState[x + 1] = 1
            ans += abs(dist[x] - dist[x + 1])
            q.append(x + 1)
    return ans


n = list(map(int, input().split()))
state = list(map(int, input().split()))
m = list(map(int, input().split()))
dist = list(map(int, input().split()))
print(solve(state, dist))