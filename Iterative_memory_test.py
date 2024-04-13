import numpy as np
import tracemalloc
import linecache
import os
from Geeksforgeeks_Floyds_Algorithm import floydWarshall
def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)
    print(f"Top {limit} lines")
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print(f"#{index}: {filename}:{frame.lineno}: {stat.size / 1024:.1f} KiB")
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print(f"    {line}")

tracemalloc.start()

if __name__ == "__main__":
    INF=9999

    graph = [
        [0, 3, INF, 7, 9, 9],
        [8, 0, 2, INF, 3, 5],
        [5, INF, 0, 1, INF, 6],
        [2, INF, INF, 0, 2, 1],
    ]
    # Function call
    floydWarshall(graph)

snapshot = tracemalloc.take_snapshot()
display_top(snapshot)
