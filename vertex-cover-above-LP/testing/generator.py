from graph import Graph

def generate_random_graph(num_vertices, num_edges, seed=None):
    import random
    random.seed(seed)

    V = range(num_vertices)
    E_full = []

    for i in V:
        for j in range(i + 1, num_vertices):
            E_full.append((i, j))

    E = random.sample(E_full, num_edges)

    return Graph(V, E)