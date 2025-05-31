from graph import Graph

def create_bipartite_graph(graph):
    """Creates a bipartite graph based on the given graph"""

    new_vertices = graph.vertices()
    new_offset = max(new_vertices) + 1

    new_vertices += [x + new_offset for x in new_vertices]

    new_edges = []

    for u in graph.vertices():
        for v in graph.neighbors(u):
            new_edges.append((u, v + new_offset))

    return Graph(new_vertices, new_edges)