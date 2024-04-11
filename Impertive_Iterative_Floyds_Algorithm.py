import numpy as np

# This is a basic imperative iterative code for Floyd's Algorithm provided from The University of Liverpool not using
# Itertools and using numpy instead of sys #


# It provides the following example of a distance matrix with nodes 0, 1,2 and 3 #

INF = np.inf

graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
             ]

MAX_LENGTH = len(graph[0])


def floyd(distance):
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                if start_node == end_node:
                    distance[start_node][end_node] = 0
                else:
                    distance[start_node][end_node] = min(
                        distance[start_node][end_node],
                        distance[start_node][intermediate] + distance[intermediate][end_node]
                    )

    return print(distance)


floyd(graph)
