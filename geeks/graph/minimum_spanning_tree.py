#User function Template for python3
from queue import PriorityQueue


class Solution:

    def insert_pq(self, pq, data):
        pq.put((data[1], data[0]))

    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        print(adj)

        m_set = [False for _ in range(V)]
        pq = PriorityQueue()
        for i in adj[0]:
            self.insert_pq(pq, i)
        result = 0
        m_set[0] = True
        while pq.empty() == False:
            u = pq.get()

            if m_set[u[1]] is False:
                result += u[0]
                m_set[u[1]] = True
                for i in adj[u[1]]:
                    if m_set[i[0]] == False:
                        self.insert_pq(pq, i)
            else:
                continue
        return result


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