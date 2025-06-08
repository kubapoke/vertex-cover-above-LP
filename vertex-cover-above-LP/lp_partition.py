from collections import deque
from graph import Graph

def create_bipartite_graph(graph):
    """Creates a bipartite graph based on the given graph"""

    old_vertices = graph.vertices()
    new_offset = max(old_vertices) + 1

    new_vertices = [x + new_offset for x in old_vertices]

    new_edges = []

    for u in old_vertices:
        for v in graph.neighbors(u):
            new_edges.append((u, v + new_offset))

    return Graph(old_vertices + new_vertices, new_edges), old_vertices, new_vertices, new_offset

def bipartite_maximum_matching(graph, U, V):
    """Hopcroft-Karp algorithm for maximum matching in a bipartite graph"""

    pair_u = {u: None for u in U}
    pair_v = {v: None for v in V}
    dist = {}

    def bfs():
        queue = deque()
        for u in U:
            if pair_u[u] is None:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[None] = float('inf')

        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in graph.neighbors(u):
                    u_prime = pair_v[v]
                    if dist.get(u_prime, float('inf')) == float('inf'):
                        dist[u_prime] = dist[u] + 1
                        queue.append(u_prime)
        return dist[None] != float('inf')

    def dfs(u):
        if u is not None:
            for v in graph.neighbors(u):
                u_prime = pair_v[v]
                if dist.get(u_prime, float('inf')) == dist[u] + 1:
                    if dfs(u_prime):
                        pair_u[u] = v
                        pair_v[v] = u
                        return True
            dist[u] = float('inf')
            return False
        return True

    matching = 0
    while bfs():
        for u in U:
            if pair_u[u] is None:
                if dfs(u):
                    matching += 1
    return pair_u, pair_v

def bipartite_minimum_vertex_cover(graph, U, V):
    """Implementation of Konig's theorem for finding minimum vertex cover in a bipartite graph"""

    pair_u, pair_v = bipartite_maximum_matching(graph, U, V)

    visited_u = set()
    visited_v = set()
    queue = deque()

    for u in U:
        if pair_u[u] is None:
            queue.append(u)
            visited_u.add(u)

    while queue:
        u = queue.popleft()
        for v in graph.neighbors(u):
            if v not in visited_v:
                visited_v.add(v)
                u_prime = pair_v[v]
                if u_prime is not None and u_prime not in visited_u:
                    visited_u.add(u_prime)
                    queue.append(u_prime)

    cover_U = [u for u in U if u not in visited_u]
    cover_V = [v for v in V if v in visited_v]

    return cover_U, cover_V

def partition(graph):
    """Creates an LP partition of the given graph for the vertex cover problem"""

    bipartite_graph, U, V, offset = create_bipartite_graph(graph)
    cover_U, cover_V = bipartite_minimum_vertex_cover(bipartite_graph, U, V)

    result = {0: [],
              0.5: [],
              1: []}

    for u in U:
        lp_sum = 0
        if u in cover_U:
            lp_sum += 0.5
        if u + offset in cover_V:
            lp_sum += 0.5
        result[lp_sum].append(u)

    return result