from graph import Graph
from vertex_cover import vertex_cover

def verify(graph, cover, k):
    # Check if all edges are covered
    for u in graph.vertices():
        for v in graph.neighbors(u):
            if u not in cover and v not in cover:
                return False

    # Check if cover size does not exceed k
    return k >= len(cover)
