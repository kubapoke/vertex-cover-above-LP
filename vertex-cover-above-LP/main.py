from graph import Graph
from vertex_cover import vertex_cover

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (2, 6), (3, 7), (4, 7),
        (5, 8), (6, 8), (7, 9), (8, 9),
        (3, 4), (5, 6), (0, 9)
    ]
    graph = Graph(range(10), edges)

    result, cover = vertex_cover(graph, 6)

    print(result, cover)