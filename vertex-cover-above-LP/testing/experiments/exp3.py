from graph import Graph
from testing.utilities.verifier import verify
from vertex_cover import vertex_cover
from mtx_to_graph import load_mtx_file

if __name__ == '__main__':
    filepath = '../mtx_graphs/web-polblogs.mtx'
    known_optimal_size = 244

    vertices, edges = load_mtx_file(filepath)
    graph = Graph(vertices, edges)

    print(f"Testing {filepath} with known optimal size {known_optimal_size}")

    result_low, cover_low = vertex_cover(graph, known_optimal_size - 1)
    assert not result_low, f"Unexpectedly found cover of size {known_optimal_size - 1}"

    print("Correctly failed to find cover with k =", known_optimal_size - 1)

    result_opt, cover_opt = vertex_cover(graph, known_optimal_size)
    assert result_opt, f"Failed to find cover of size {known_optimal_size} when it should exist"
    assert verify(graph, set(cover_opt), known_optimal_size), "Cover verification failed"

    print(f"Found valid vertex cover of size {known_optimal_size}: {cover_opt}")
