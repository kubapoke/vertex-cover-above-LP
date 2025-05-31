from collections import defaultdict

class Graph:
    """Undirected graph class"""

    def __init__(self, edges):
        self._graph = defaultdict(set)
        self.add_edges(edges)

    def __len__(self):
        """Returns number of vertices in graph"""

        return len(self._graph)

    def __str__(self):
        """Returns string representing neighbors of each vertex in graph"""

        lists = []
        for v, neighbors in self._graph.items():
            lists.append("{}: {}".format(v, neighbors))

        return "\n".join(lists)

    def add_edges(self, edges):
        """Adds edges to graph"""

        for u, v in edges:
            self.add(u, v)

    def add(self, u, v):
        """Adds a single edge to graph"""

        self._graph[u].add(v)
        self._graph[v].add(u)

    def remove(self, u, v):
        """Removes a single edge from graph"""

        self._graph[u].remove(v)
        self._graph[v].remove(u)

        if len(self._graph[u]) == 0:
            self._graph.pop(u)
        if len(self._graph[v]) == 0:
            self._graph.pop(v)

    def pop(self, v):
        """Removes a single vertex from graph"""

        for u in self._graph[v].copy():
            self.remove(u, v)
