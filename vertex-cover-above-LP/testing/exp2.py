from testing.brute_solver import brute_solve
from testing.generator import generate_random_graph
from testing.verifier import verify
from vertex_cover import vertex_cover

if __name__ == "__main__":
    num_vertices = 10  # 1000 # 10000 # 100000 # 1000000
    num_edges = 35
    repetitions = 1000

    for i in range(repetitions):
        graph = generate_random_graph(num_vertices, num_edges, i)

        brute_solution = brute_solve(graph)
        k = len(brute_solution)

        false_result, false_cover = vertex_cover(graph, k - 1)
        true_result, true_cover = vertex_cover(graph, k)

        if false_result == False and true_result == True and verify(graph, true_cover, k):
            print("Experiment passed -- The vertex cover finds a solution for the found minimum k and does not for a lesser one.")
        elif false_result == True:
            print("Experiment failed -- Found a solution smaller than the smallest one.")
            break
        elif true_result == False:
            print("Experiment failed -- Didn't find a solution of the found size.")
            break
        else:
            print("Experiment failed -- The found solution is not correct.")
            break