import copy
from collections import defaultdict

class Graph:
    """Undirected graph class"""

    def __init__(self, vertices, edges):
        self._graph = defaultdict(set)
        self._vertices = set(vertices)
        self.add_edges(edges)

    def __len__(self):
        """Returns number of vertices in graph"""

        return self.vertex_count()

    def __str__(self):
        """Returns string representing neighbors of each vertex in graph"""

        if self.vertex_count() == 0:
            return "The graph is empty"

        lists = []
        for v  in  self._vertices:
            neighbors = "{}"

            if v in self._graph and len(self._graph[v]) > 0:
                neighbors = self._graph[v]

            lists.append("{}: {}".format(v, neighbors))

        return "\n".join(lists)

    def verify_existence(self, v):
        """Throws an exception if vertex does not exist"""

        if v not in self._vertices:
            raise KeyError("Vertex {} not in graph".format(v))

    def add_edges(self, edges):
        """Adds edges to graph"""

        for u, v in edges:
            self.add(u, v)

    def add(self, u, v):
        """Adds a single edge to graph"""

        self.verify_existence(u)
        self.verify_existence(v)

        self._graph[u].add(v)
        self._graph[v].add(u)

    def remove(self, u, v):
        """Removes a single edge from graph"""

        self.verify_existence(u)
        self.verify_existence(v)

        self._graph[u].remove(v)
        self._graph[v].remove(u)

    def pop(self, v):
        """Removes a single vertex from graph"""

        self.verify_existence(v)

        for u in self._graph[v].copy():
            self.remove(u, v)

        self._vertices.remove(v)
        self._graph.pop(v)

    def degree(self, v):
        """Returns the degree of vertex in graph"""

        self.verify_existence(v)

        if v not in self._graph:
            return 0

        return len(self._graph[v])

    def vertex_count(self):
        """Returns number of vertices in graph"""

        return len(self._vertices)

    def edge_count(self):
        """Returns number of edges in graph"""

        return sum(len(neighbors) for neighbors in self._graph.values()) // 2

    def vertices(self):
        """Returns all vertices in graph"""

        return list(self._vertices.copy())

    def adjacent(self, u, v):
        """Returns whether vertex u is adjacent to vertex v"""

        self.verify_existence(u)
        self.verify_existence(v)

        return u in self._graph[v] and v in self._graph[u]

    def neighbors(self, v):
        """Returns all neighbors of vertex in graph"""

        self.verify_existence(v)

        if v not in self._graph:
            return []

        return list(self._graph[v].copy())

    def induced_subgraph(self, V):
        """Returns an induced subgraph based on the vertex subset V"""

        new_edges = []

        for u in V:
            for v in V:
                if self.adjacent(u, v):
                    new_edges.append((u, v))

        return Graph(V, new_edges)

    def copy_without_vertices(self, V):
        """Returns a copy of graph with vertices in V removed from graph"""

        new_graph = copy.deepcopy(self)

        for v in V:
            new_graph.pop(v)

        return new_graph
