from graph import Graph
from kernel import find_kernel

if __name__ == '__main__':

    edges = [(0, 1), (0, 2), (0, 3), (0, 4)]
    graph = Graph(range(5), edges)

    print("{}\n".format(graph))

    graph, k = find_kernel(graph, 3)

    print("{}\n{}".format(graph, k))