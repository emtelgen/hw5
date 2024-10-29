#I utilized LLMs to create the graph for me

import random
import time
import matplotlib.pyplot as plt
from mergesort import merge_sort
from insertionsort import insertion_sort

def time_sort(sort_function, array, repetitions=1000):
    total_time = 0
    for _ in range(repetitions):
        start_time = time.time()
        sort_function(array)
        total_time += time.time() - start_time
    return total_time / repetitions  

n_values = []
merge_sort_times = []
insertion_sort_times = []

for n in range(1, 301, 5):
    random_array = [random.randint(1, 10000) for _ in range(n)]
    merge_time = time_sort(merge_sort, random_array.copy())
    insertion_time = time_sort(insertion_sort, random_array.copy())
    
    n_values.append(n)
    merge_sort_times.append(merge_time)
    insertion_sort_times.append(insertion_time)

plt.figure(figsize=(10, 6))
plt.plot(n_values, merge_sort_times, label='Merge Sort', marker='o')
plt.plot(n_values, insertion_sort_times, label='Insertion Sort', marker='o')
plt.xlabel('Size of Array (n)')
plt.ylabel('Average Time (seconds)')
plt.title('Performance Comparison of Merge Sort and Insertion Sort')
plt.legend()
plt.grid()

plt.show()
