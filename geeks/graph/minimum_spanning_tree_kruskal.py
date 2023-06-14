#User function Template for python3
from queue import PriorityQueue


class Solution:

    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # kruskal's Algorithm
        visited = [False] * V
        edges = set()
        for i in range(V):
            for j in adj[i]:
                edges.add((i, j[0], j[1]))
        edges = list(edges)

        ans = 0

        edges.sort(key=lambda arr: arr[2])
        for i in edges:
            if visited[i[0]] is True and visited[i[1]] is True:
                continue
            else:
                ans += i[2]
                visited[i[0]] = True
                visited[i[1]] = True
        return ans


#{
# Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
# } Driver Code Ends