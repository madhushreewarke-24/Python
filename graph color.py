def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def solve_graph_coloring(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c

            if solve_graph_coloring(graph, m, color, v + 1):
                return True

            color[v] = 0  # Backtracking

    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)

    if solve_graph_coloring(graph, m, color, 0):
        print("Solution exists:")
        print(color)
    else:
        print("No solution exists")

# Example graph (Adjacency Matrix)
graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

m = 3
graph_coloring(graph, m)