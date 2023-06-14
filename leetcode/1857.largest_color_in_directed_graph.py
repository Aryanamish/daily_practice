class Solution:
    def largestPathValue(self, colors, edges):
        graph = [[] for _ in range(len(colors))]
        for e in edges:
            graph[e[0]].append(e[1])
        self.colors = colors

        self.color_dict = {i:0 for i in colors}
        self.max_color = 0
        return self.detectCycle(graph)

    def highest_color(self, graph):
        recStack = [False for _ in range(len(graph))]
        visited = [False for _ in range(len(graph))]

        for node in range(len(graph)):
            if visited[node] is False:
                self.dfs_color(graph, node, recStack, visited)

    def dfs_color(self, graph, node, recStack, visited):
        self.color_dict[self.colors[node]] += 1
        visited[node] = True
        recStack[node] = True
        for n in graph[node]:
            if recStack[n] is False:
                self.dfs_color(graph, n, recStack, visited)
        recStack[node] = False
        for i in self.color_dict:
            self.max_color = max(self.max_color, self.color_dict[i]) 
        self.color_dict[self.colors[node]] -= 1
        

    def dfs(self, graph, node, visited, recStack):
        self.color_dict[self.colors[node]] += 1

        recStack[node] = True
        visited[node] = True
        for n in graph[node]:
            if recStack[n] is True:
                recStack[n] = False
                return True # Cycle is detected
            if recStack[n] is False:
                if self.dfs(graph, n, visited, recStack) is True:
                    return True
        
        recStack[node] = False
        for i in self.color_dict:
            self.max_color = max(self.max_color, self.color_dict[i]) 
        self.color_dict[self.colors[node]] -= 1

            
        

    def detectCycle(self, graph):
        visited = [False] * len(graph)
        recStack = [False] * len(graph)

        for node in range(len(graph)):
            if visited[node] is False:
                if self.dfs(graph, node, visited, recStack) is True:
                    return -1
        return self.max_color
            



        

if __name__ == '__main__':
    s = Solution()
    print(s.largestPathValue("nnllnzznn", [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]))
        