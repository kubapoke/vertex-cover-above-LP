from graph import Graph

def remove_vertices(graph, k):
    """Removes vertices in graph with degree larger than k and returns number of vertices removed"""

    changes = False
    reduced_graph = graph.copy()
    chosen = set()

    for v in reduced_graph.vertices():
        if reduced_graph.degree(v) == 0:
            reduced_graph.pop(v)
            changes = True

        if reduced_graph.degree(v) > k:
            reduced_graph.pop(v)
            changes = True
            chosen.add(v)
            k -= 1

    return changes, reduced_graph, chosen, k

def reduce_via_vertex_removal(graph, k):
    """Given a graph and parameter k, the function returns the kernel instance for the vertex cover problem using the standard reduction algorithm"""

    changes = True
    reduced_graph = graph.copy()
    chosen = set()

    while changes:
        changes, reduced_graph, new_chosen, k = remove_vertices(graph, k)
        chosen |= new_chosen

    return reduced_graph, chosen, k

def reduce_via_lp_partition(graph, k, lp_partition):
    """Reduces a graph via a giver LP partition"""

    chosen = set(lp_partition[1])

    half_graph = graph.induced_subgraph(lp_partition[0.5])

    return half_graph, chosen, k - len(chosen)