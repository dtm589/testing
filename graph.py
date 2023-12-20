class Graph:
    def __init__(self, num_vertices):
        self.graph = []
        for num in range(num_vertices):
            self.graph.append([False] * num_vertices)
    
    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True