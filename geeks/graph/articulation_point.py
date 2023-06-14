#User function Template for python3

import sys

sys.setrecursionlimit(10**6)


class Solution:

    #Function to return Breadth First Traversal of given graph.
    def DFS(self, adj, v, parent, low, disc, ans, visited):
        low[v] = disc[v] = self.time
        self.time += 1
        visited[v] = True
        child = 0
        for u in adj[v]:
            # if the child is equal to itself or is the parent
            if u == v or u == parent[v]:
                continue

            # if this node is not visited then visit it
            if visited[u] is False:
                child += 1
                parent[u] = v
                self.DFS(adj, u, parent, low, disc, ans, visited)

                # change the low of u's parents i.e v if u has a lower value than v
                low[v] = min(low[v], low[u])

                # if child > 1 and parent == -1 for root node
                # low of current node is greater than discovery time
                # of v current node parent then sure u is articulation point
                if (child > 1 and parent[v] == -1) or (low[u] >= disc[v]
                                                       and parent[v] != -1):
                    ans.add(v)
            else:
                # this is a backedge so update the low value to discovery time of u
                low[v] = min(low[v], disc[u])

    def articulationPoints(self, V, adj):
        low = [-1] * V
        disc = [-1] * V
        ans = set()
        visited = [False] * V
        self.time = 0
        parent = [-1] * V
        for i in range(V):
            if visited[i] is False:
                self.DFS(adj, 0, parent, low, disc, ans, visited)
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
        ob = Solution()
        ans = ob.articulationPoints(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends