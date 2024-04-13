from Graph_data import graph  # Importing graph data

"""This is a recursive version for the Floyd's algorthm
this has been amended from version 1, simplifying by using a 
data source file"""


def floyd(graph):
    max_length = len(graph)

    distance = [list(row) for row in graph]

    def floyd_recursive(k, x, y):  # Recursive formula
        if k == max_length:
            return
        distance[x][y] = min(distance[x][y], distance[x][k] + distance[k][y])
        floyd_recursive(k + 1, x, y)

    for k in range(max_length):
        for x in range(max_length):
            for y in range(max_length):
                floyd_recursive(k, x, y)

    return distance


if __name__ == "__main__":  # running the code within this nodule
    shortest_paths = floyd(graph)
    for row in shortest_paths:
        print(row)
