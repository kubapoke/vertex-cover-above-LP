from graph import Graph

if __name__ == '__main__':

    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 2)]
    graph = Graph(edges)

    print(graph)

    graph.remove(1, 2)
    graph.remove(0, 2)
    graph.remove(3, 2)

    print(graph)