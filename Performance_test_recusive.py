import datetime
import timeit
from Floyds_Algorithm_recursive_v2 import floyd
from Graph_data import graph

""" This module looks at the final version (v2) of 
the recursive version of my flloyd algorithm
and looks at the performance; specifcally time
using a brute force method and a 'timeit' method
"""

# Brute force test 1

start_time = datetime.datetime.now()

if __name__ == "__main__":
    shortest_paths = floyd(graph)

end_time = datetime.datetime.now()

print("The total time taken is", end_time - start_time)

# This is a test using timeit

if __name__ == "__main__":
    shortest_paths = floyd(graph)

num_iterations = 1000

elapsed_time = timeit.timeit(lambda: floyd(graph), number=num_iterations)

# Print the average time per iteration
print(f"Average time taken per iteration: {elapsed_time / num_iterations:.6f} seconds")
