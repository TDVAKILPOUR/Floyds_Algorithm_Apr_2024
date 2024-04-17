import timeit
from Geeksforgeeks_Floyds_Algorithm import floydWarshall


""" This is a performance test for the iterative Floyd formula
provided on the Geeks for Geeks website. This is a time test
using timeit
"""
INF = 9999

if __name__ == "__main__":

    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
             ]
    # Function call
    floydWarshall(graph)

num_iterations = 1000

elapsed_time = timeit.timeit(lambda: floydWarshall(graph), number=num_iterations)

# Print the average time per iteration
print(f"Average time per iteration: {elapsed_time / num_iterations:.6f} seconds")
