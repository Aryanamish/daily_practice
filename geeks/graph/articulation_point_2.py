class Solution:

    def find_points(self, adj, v, visited, disc, low, ans, parent=-1):
        disc[v] = low[v] = self.time
        self.time += 1
        visited[v] = True
        child = 0
        for u in adj[v]:
            if u == v or u == parent:
                continue
            if visited[u] is False:
                child += 1
                self.find_points(adj, u, visited, disc, low, ans, v)

                low[v] = min(low[v], low[u])
                if child > 1 and parent == -1:
                    ans.add(v)
                if low[u] >= disc[v] and parent != -1:
                    ans.add(v)
            else:
                low[v] = min(low[v], disc[u])

    def articulationPoints(self, V, adj):
        #Code here
        disc = [-1] * V
        low = [-1] * V
        visited = [False] * V
        ans = set()
        self.time = 0
        for i in range(V):
            if visited[i] is False:
                self.find_points(adj, i, visited, disc, low, ans)

        ans = list(ans)
        ans.sort()
        return ans or [-1]


#{
# Driver Code Starts

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.articulationPoints(V, adj)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends