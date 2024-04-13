import numpy as np

"""This is my first version of my Floyds Algorithm using recursion"""


def floyd(graph):
    MAX_LENGTH = len(graph)

    distance = [list(row) for row in graph]

    def floyd_recursive(k, x, y):  # Recursive formula
        if k == MAX_LENGTH:
            return
        distance[x][y] = min(distance[x][y], distance[x][k] + distance[k][y])
        floyd_recursive(k + 1, x, y)

    for k in range(MAX_LENGTH):
        for x in range(MAX_LENGTH):
            for y in range(MAX_LENGTH):
                floyd_recursive(k, x, y)

    return distance


if __name__ == "__main__":
    INF = np.inf

    graph = [
        [0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
    ]

    shortest_paths = floyd(graph)
    for row in shortest_paths:
        print(row)
