from Graph_data import graph, max_length

""" This is a basic imperative iterative code for Floyd's Algorithm provided from 
The University of Liverpool not using Itertools and using numpy instead of sys, 
it provides the following example of a distance matrix with nodes 0, 1,2 and 3 """


def floyd(distance):
    for intermediate in range(max_length):
        for start_node in range(max_length):
            for end_node in range(max_length):
                if start_node == end_node:
                    distance[start_node][end_node] = 0
                else:
                    distance[start_node][end_node] = min(
                        distance[start_node][end_node],
                        distance[start_node][intermediate] + distance[intermediate][end_node]
                    )

    return print(distance)


floyd(graph)  # excutes code
