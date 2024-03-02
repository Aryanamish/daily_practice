import json 

class Graph:
    def __init__(self) -> None:
        self.no_of_node = 0
        self.adjacent_list = {}

    def addVertex(self, node):
        if self.adjacent_list.get(node, None) is None:
            self.adjacent_list[node] = []

    def addEdge(self, node1, node2):
        if self.adjacent_list.get(node1, None) is not None and self.adjacent_list.get(node2, None) is not None:
             self.adjacent_list[node1].append(node2)
             self.adjacent_list[node2].append(node1)

    def __str__(self):
        return json.dumps(self.adjacent_list)

g = Graph()
g.addVertex('0')
g.addVertex('1')
g.addVertex('2')
g.addVertex('3')
g.addVertex('4')
g.addVertex('5')
g.addVertex('6')

g.addEdge('3', '1')
g.addEdge('3', '4')
g.addEdge('4', '2')
g.addEdge('4', '5')
g.addEdge('1', '2')
g.addEdge('1', '0')
g.addEdge('0', '2')
g.addEdge('6', '5')

print(g)
