from itertools import combinations
from testing.verifier import verify

def all_subsets(collection):
    for r in range(len(collection) + 1):
        for subset in combinations(collection, r):
            yield subset

def brute_solve(graph):
    for vertex_subset in all_subsets(graph.vertices()):
        if verify(graph, vertex_subset, len(vertex_subset)):
            return vertex_subset
    return None