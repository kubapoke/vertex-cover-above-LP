from graph import Graph
from vertex_cover import vertex_cover
from verifier import verify

def generate_random_graph(num_vertices, num_edges):
    import random
    set_random_seed = 42  # For reproducibility
    random.seed(set_random_seed)
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    return Graph(range(num_vertices), list(edges))


if __name__ == '__main__':
    import time

    num_vertices = 1000 # 1000 # 10000 # 100000 # 1000000
    num_edges = 10
    graph = generate_random_graph(num_vertices, num_edges)
   
    
    start_time = time.time()
    k = 100
    result, cover = vertex_cover(graph, k)
    end_time = time.time()

    #print(f"Result: {result}, Cover: {cover}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    if(result):
        if verify(graph, cover, k):
            print("The cover is valid.")
        else:
            print("The cover is invalid.")
    