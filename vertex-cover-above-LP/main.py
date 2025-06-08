from graph import Graph
from vertex_cover import vertex_cover

if __name__ == '__main__':

    edges = [(3, 4), (4, 2), (0, 2), (1, 4)]
    graph = Graph(range(5), edges)

    result, cover = vertex_cover(graph, 2)

    print(result, cover)