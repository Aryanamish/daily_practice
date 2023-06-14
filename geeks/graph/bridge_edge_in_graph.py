#User function Template for python3


class Solution:

    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        try:
            adj[c].remove(d)

        except:
            pass

        try:
            adj[d].remove(c)
        except:
            pass

        visited = [False for _ in range(V)]
        count = 0
        for i in range(V):
            if visited[i] is False:
                if count == 1:
                    return 1
                count += 1
                self.DFS(adj, i, visited)

        return 0

    def DFS(self, adj, s, visited):
        visited[s] = True

        for i in adj[s]:
            if visited[i] is False:
                self.DFS(adj, i, visited)


#{
# Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
            adj[b].append(a)

        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i]))

        c, d = map(int, input().split())
        ob = Solution()

        print(ob.isBridge(V, adj, c, d))
# } Driver Code Ends