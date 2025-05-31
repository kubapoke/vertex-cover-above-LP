from kernel import find_kernel

def vertex_cover(graph, k, find_cover = False):
    """Answers the question: does the graph contain a vertex cover of size k?"""

    graph, k = find_kernel(graph, k)

    if graph.edge_count() == 0:
        return True
    if k == 0:
        return False

