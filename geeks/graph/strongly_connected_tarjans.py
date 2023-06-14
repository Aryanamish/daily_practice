#User function Template for python3
import numpy as np


class Solution:

    #Function to return a list of lists of integers denoting the members
    #of strongly connected components in the given graph.
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
            if visited[i] == True:
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

    def tarjans(self, V, adj):
        ans = []
        self.time = 0
        dis = np.full((V, ), -1, dtype=int)
        low = np.full((V, ), -1, dtype=int)
        visited = np.full((V, ), False, dtype=bool)
        stack = []
        for i in range(V):
            if dis[i] == -1:
                self.tarjansDFS(adj, i, visited, stack, dis, low, ans)

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

        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i]))

        ob = Solution()

        ptr = ob.tarjans(V, adj)

        for i in range(len(ptr)):
            for j in range(len(ptr[i])):
                if j == len(ptr[i]) - 1:
                    print(ptr[i][j], end="")
                else:
                    print(ptr[i][j], end=" ")
            print(",", end="")
        print()
# } Driver Code Ends