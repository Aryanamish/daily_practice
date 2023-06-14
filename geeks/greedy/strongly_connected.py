# Python implementation of Kosaraju's algorithm to print all SCCs


class Solution:

    def tarjansDFS(self, adj, u, visited, stack, dis, low, ans):
        dis[u] = self.time

        low[u] = self.time

        self.time += 1

        visited[u] = True

        stack.append(u)

        for i in adj[u]:

            if dis[i] == -1:

                self.tarjansDFS(adj, i, visited, stack, dis, low, ans)

                low[u] = min(low[i], low[u])

            elif visited[i] == True:

                low[u] = min(low[i], low[u])

        if low[u] == dis[u]:
            temp = []

            while len(stack) > 0 and dis[stack[-1]] != low[stack[-1]]:

                x = stack.pop()

                temp.append(x)

                visited[x] = False

            x = stack.pop()

            temp.append(x)

            visited[x] = False
            temp.sort()
            ans.append(temp)

    def SCC(self, V, adj):
        ans = []

        self.time = 0

        dis = [-1 for _ in range(V)]

        low = [-1 for _ in range(V)]

        visited = [False for _ in range(V)]

        stack = []

        for i in range(V):

            if dis[i] == -1:

                self.tarjansDFS(adj, i, visited, stack, dis, low, ans)
        ans.sort()
        return ans


t = int(input())

for _ in range(t):

    V, E = list(map(int, input().strip().split()))

    adj = [[] for i in range(V)]

    for _ in range(E):

        a, b = map(int, input().strip().split())

        adj[a - 1].append(b - 1)

    s = Solution()
    ans = s.SCC(V, adj)

    a = 0

    for comp in ans:

        a = max(a, len(comp))
    print(a)

# 1

# 5 7

# 1 2

# 2 1

# 1 3

# 2 3

# 3 4

# 4 5

# 5 3