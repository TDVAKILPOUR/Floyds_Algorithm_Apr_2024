import unittest
from Floyds_Algorithm_recursive_v1 import floyd  # Adjust the import based on your actual module or function

class TestFloydGraph(unittest.TestCase):
    def test_graph1(self):
        graph = [
            [0, 5, 1, 2],
            [1, 2, 2, 2],
            [0, 3, 4, 5],
            [4, 5, 6, 7]
        ]

        expected_result = [[0, 4, 1, 2], [1, 2, 2, 2], [0, 3, 1, 2], [4, 5, 5, 6]]

        self.assertEqual(floyd(graph), expected_result)

if __name__ == '__main__':
    unittest.main()
