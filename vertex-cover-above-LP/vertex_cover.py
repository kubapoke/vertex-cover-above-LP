from kernel import reduce_via_lp_partition, reduce_via_vertex_removal
from lp_partition import partition

def only_halves(solution):
    """Checks whether an LP solution contains only 1/2 values"""

    return len(solution[0]) == 0 and len(solution[1]) == 0

def solution_value(solution):
    """Returns the value of an LP solution"""

    return len(solution[1]) + len(solution[0.5]) * 0.5

def vertex_cover(graph, k):
    """Answers the question: does the graph contain a vertex cover of size k? If it does - returns it"""

    if graph.edge_count() == 0:
        return True, set()

    if k == 0:
        return False, None

    lp_partition = partition(graph)
    lp_value = solution_value(lp_partition)

    return vertex_cover_branching(graph, k, lp_value, set())

def vertex_cover_branching(graph, k, lp_value, cover):
    """Perform the vertex cover branching algorithm on a graph recursively"""

    while True:
        if lp_value > k:
            return False, None

        lp_partition = partition(graph)
        lp_only_halves = only_halves(lp_partition)

        if lp_only_halves:
            break

        graph, newly_chosen, k = reduce_via_lp_partition(graph, k, lp_partition)
        cover |= newly_chosen

        if graph.edge_count() == 0:
            return True, cover

        if k == 0:
            return False, None

        lp_partition = partition(graph)
        lp_value = solution_value(lp_partition)

    v = graph.highest_degree()
    neighbors = graph.neighbors(v)

    # remove v
    new_graph = graph.copy_without_vertices([v])
    new_k = k - 1
    new_lp_partition = partition(new_graph)
    new_lp_value = solution_value(new_lp_partition)
    new_cover = cover | {v}
    result, result_cover = vertex_cover_branching(new_graph, new_k, new_lp_value, new_cover)
    if result:
        return result, result_cover

    # remove neighbors
    new_graph = graph.copy_without_vertices(neighbors)
    new_k = k - len(neighbors)
    new_lp_partition = partition(new_graph)
    new_lp_value = solution_value(new_lp_partition)
    new_cover = cover | set(neighbors)
    result, new_cover = vertex_cover_branching(new_graph, new_k, new_lp_value, new_cover)
    if result:
        return result, new_cover

    return False, None
