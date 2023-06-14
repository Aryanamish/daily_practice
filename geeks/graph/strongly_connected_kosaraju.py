#User function Template for python3


class Solution:

    #Function to find number of strongly connected components in the graph.
    def DFS(self, adj, s, visited, stack=[]):
        visited[s] = True

        for i in adj[s]:
            if visited[i] is False:
                # pass
                self.DFS(adj, i, visited, stack)

        stack.append(s)

    def kosaraju(self, V, adj):
        # code here
        visited = [False for _ in range(V)]
        stack = []

        for i in range(V):
            if visited[i] is False:
                self.DFS(adj, i, visited, stack)

        new_adj = [[] for j in range(V)]
        for i in range(V):
            visited[i] = False
            for j in adj[i]:
                new_adj[j].append(i)
        ans = 0
        while len(stack) > 0:
            i = stack.pop()
            if visited[i] is False:
                ans += 1
                self.DFS(adj, i, visited)
        return ans


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
        ob = Solution()

        print(ob.kosaraju(V, adj))
# } Driver Code Ends