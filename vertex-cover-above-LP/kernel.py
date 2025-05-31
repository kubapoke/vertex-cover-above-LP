from graph import Graph

def false_instance():
    """Returns a simple NO instance for the vertex cover problem"""

    return Graph(range(2), [(0, 1)]), 0

def remove_vertices(graph, k):
    """Removes vertices in graph with degree larger than k and returns number of vertices removed"""

    removed = 0

    for v in graph.vertices():
        if graph.degree(v) == 0:
            graph.pop(v)
            removed += 1

    for v in graph.vertices():
        if graph.degree(v) > k:
            graph.pop(v)
            removed += 1
            k -= 1

    return removed, k

def find_kernel(graph, k):
    """Given a graph and parameter k, the function returns the kernel instance for the vertex cover problem"""

    removed = 1

    while removed > 0:
        removed, k = remove_vertices(graph, k)

    if graph.vertex_count() > k * k + k or graph.edge_count() > k * k:
        return false_instance()

    return graph, k