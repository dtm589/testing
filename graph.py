class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])
            
    def adjacent_nodes(self, node):
        outcome = []
        for item in self.graph[node]:
            outcome.append(item)
        return outcome
    
    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()
            
    def unconnected_vertices(self):
        outcome = []
        for entry in self.graph:
            if self.graph[entry] == set():
                outcome.append(entry)
        return outcome
    
    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)
        while len(to_visit) >= 1:
            place = to_visit.pop(0)
            visited.append(place)
            sorted_list = sorted(self.graph[place]) # how do i get the neighbors
            for neigbor in sorted_list:
                if neigbor not in visited and neigbor not in to_visit:
                    to_visit.append(neigbor)
        return visited