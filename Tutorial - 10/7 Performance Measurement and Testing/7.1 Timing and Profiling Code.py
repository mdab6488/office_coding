# The timeit module provides a simple way to measure the execution time of small code snippets, which is essential for identifying performance bottlenecks in web applications.

from timeit import Timer
import time

# Compare performance of different approaches
def slow_function():
    result = []
    for i in range(1000):
        result.append(i * 2)
    return result

def fast_function():
    return [i * 2 for i in range(1000)]

# Time both functions
t1 = Timer('slow_function()', 'from __main__ import slow_function')
t2 = Timer('fast_function()', 'from __main__ import fast_function')

print(f"Slow function time: {t1.timeit(number=1000):.3f} seconds")
print(f"Fast function time: {t2.timeit(number=1000):.3f} seconds")

# Practical example: timing database queries
def query_database():
    # Simulate database query
    time.sleep(0.01)
    return ["result1", "result2", "result3"]

# Time the query execution
query_time = timeit.timeit(query_database, number=10)
print(f"Average query time: {query_time / 10:.3f} seconds")

# For more comprehensive performance analysis, Python provides the profile and cProfile modules which give detailed insights into function call times and frequencies 
