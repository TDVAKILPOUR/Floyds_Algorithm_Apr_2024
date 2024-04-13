import unittest
from Floyds_Algorithm_recursive_v2 import floyd
from Graph_data import graphtest, expected_result

""" This is a unit test code to test the function "floyd", 
which is the recursive algorthim. It looks to test data, 
and expected result. 
"""


class TestFloydGraph(unittest.TestCase):
    def test_graph1(self):
        graph = graphtest

        self.assertEqual(floyd(graph), expected_result)


if __name__ == '__main__':
    unittest.main()
