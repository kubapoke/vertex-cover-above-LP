from testing.utilities.verifier import verify
from vertex_cover import vertex_cover
from testing.utilities.generator import generate_random_graph

if __name__ == '__main__':
    import time

    num_vertices = 1000 # 1000 # 10000 # 100000 # 1000000
    num_edges = 10
    graph = generate_random_graph(num_vertices, num_edges, 42)

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
    