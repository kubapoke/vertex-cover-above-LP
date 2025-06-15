import unittest
from graph import Graph
from vertex_cover import vertex_cover

class TestVertexCover(unittest.TestCase):

    def test_empty_graph(self):
        graph = Graph([], [])
        result, cover = vertex_cover(graph, 0)
        self.assertTrue(result)
        self.assertEqual(cover, set())

    def test_single_edge(self):
        graph = Graph([0, 1], [(0, 1)])
        result, cover = vertex_cover(graph, 1)
        self.assertTrue(result)
        self.assertIn(cover, [{0}, {1}])

    def test_triangle(self):
        graph = Graph([0, 1, 2], [(0, 1), (1, 2), (2, 0)])
        result, cover = vertex_cover(graph, 2)
        self.assertTrue(result)
        self.assertEqual(len(cover), 2)

    def test_unsatisfiable_triangle(self):
        graph = Graph([0, 1, 2], [(0, 1), (1, 2), (2, 0)])
        result, cover = vertex_cover(graph, 1)
        self.assertFalse(result)

    def test_moderate_graph(self):
        edges = [
            (0, 1), (0, 2), (1, 3), (1, 4),
            (2, 5), (2, 6), (3, 7), (4, 7),
            (5, 8), (6, 8), (7, 9), (8, 9),
            (3, 4), (5, 6), (0, 9)
        ]
        graph = Graph(range(10), edges)
        result, cover = vertex_cover(graph, 6)
        self.assertIsInstance(result, bool)
        if result:
            for u, v in edges:
                self.assertTrue(u in cover or v in cover)

if __name__ == '__main__':
    unittest.main()
