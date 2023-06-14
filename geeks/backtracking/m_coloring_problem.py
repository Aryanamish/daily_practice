#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def is_possible(graph, colors_assign, v, c):
    for conn in range(len(graph[v])):
        if graph[v][conn] == 1 and colors_assign[conn] == c:
            return False
    return True


def solve(graph, color, colors_assign, no_of_vertices, color_count,
          curr_vertix):
    if color_count == no_of_vertices:
        return True

    for v in range(curr_vertix, no_of_vertices):
        for c in range(color):
            if is_possible(graph, colors_assign, v, c):
                colors_assign[v] = c
                if solve(graph, color, colors_assign, no_of_vertices,
                         color_count + 1, v + 1):
                    return True
                colors_assign[v] = None

    return False


def graphColoring(graph, color, no_of_vertices):
    colors_assign = {v: None for v in range(no_of_vertices)}
    assigne_count = 0
    return solve(graph, color, colors_assign, no_of_vertices, 0, 0)


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt] - 1][list[cnt + 1] - 1] = 1
            graph[list[cnt + 1] - 1][list[cnt] - 1] = 1
            cnt += 2
        if (graphColoring(graph, k, V) == True):
            print(1)
        else:
            print(0)

        t = t - 1

# } Driver Code Ends