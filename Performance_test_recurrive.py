import numpy as np
import datetime
import timeit
from Floyds_Algorithm_recursive_v1 import floyd

#Brute force test 1

start_time = datetime.datetime.now()


if __name__ == "__main__":
    INF = np.inf

    graph = [
        [0, 3, INF, 7, 9, 9],
        [8, 0, 2, INF, 3, 5],
        [5, INF, 0, 1, INF,6],
        [2, INF, INF, 0, 2, 1],
    ]

    shortest_paths = floyd(graph)
    for row in shortest_paths:
        print(row)


end_time = datetime.datetime.now()

print("The total time taken is", end_time-start_time)

# This is a test using timeit

if __name__ == "__main__":
    INF = np.inf

    graph = [
        [0, 3, INF, 7, 9, 9],
        [8, 0, 2, INF, 3, 5],
        [5, INF, 0, 1, INF,6],
        [2, INF, INF, 0, 2, 1],
    ]

    shortest_paths = floyd(graph)
    for row in shortest_paths:
        print(row)

num_iterations = 1000

elapsed_time = timeit.timeit(lambda: floyd(graph), number=num_iterations)

# Print the average time per iteration
print(f"Average time per iteration: {elapsed_time / num_iterations:.6f} seconds")




