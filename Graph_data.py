import numpy as np

""" This is a file for the graph data
to be used in the iterative and recursive 
algorithms, it also contains the graph test data"""

INF = np.inf

graph = [
    [0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0]
]  # The graph data provided as part of assignment

graphtest = [
    [0, 5, 1, 2],
    [1, 2, 2, 2],
    [0, 3, 4, 5],
    [4, 5, 6, 7]
]

graph_gfg = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]

max_length = len(graph[0])

expected_result = [[0, 4, 1, 2], [1, 2, 2, 2], [0, 3, 1, 2], [4, 5, 5, 6]]
