import time
import random
import matplotlib.pyplot as plt

# Insertion Sort implementation
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr, left, right, k):
    if right - left + 1 <= k:
        insertion_sort(arr, left, right)
    else:
        if left < right:
            mid = (left + right) // 2
            merge_sort(arr, left, mid, k)  
            merge_sort(arr, mid + 1, right, k)  
            merge(arr, left, mid, right) 

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def hybrid_sort(arr, min_run=32, k=16):
    n = len(arr)
    
    for i in range(0, n, k):
        insertion_sort(arr, i, min((i + k - 1), n - 1))
    
    size = k
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            end = min((start + size * 2 - 1), (n - 1))
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2

def measure_time(sort_function, arr, *args):
    start_time = time.time()
    sort_function(arr, *args)
    return time.time() - start_time

def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def test_sorts():
    n_values = [100, 500, 1000, 5000, 10000] 
    k_values = [4, 8, 16, 32, 64, 128, 256] 
    hybrid_times = []
    merge_times = []
    insertion_times = []

    for n in n_values:
        hybrid_avg_time = []
        merge_avg_time = []
        insertion_avg_time = []

        for k in k_values:
            arr = generate_random_array(n)
            hybrid_time = measure_time(hybrid_sort, arr, 32, k)
            hybrid_avg_time.append(hybrid_time)

            arr = generate_random_array(n)
            merge_time = measure_time(merge_sort, arr, 0, n - 1, k)
            merge_avg_time.append(merge_time)

            arr = generate_random_array(n)
            insertion_time = measure_time(insertion_sort, arr, 0, n - 1)
            insertion_avg_time.append(insertion_time)

        hybrid_times.append(hybrid_avg_time)
        merge_times.append(merge_avg_time)
        insertion_times.append(insertion_avg_time)

    plt.figure(figsize=(10, 6))
    for i, n in enumerate(n_values):
        plt.plot(k_values, hybrid_times[i], label=f'Hybrid Sort (n={n})', marker='o')
        plt.plot(k_values, merge_times[i], label=f'Merge Sort (n={n})', marker='x')
        #plt.plot(k_values, insertion_times[i], label=f'Insertion Sort (n={n})', marker='s')

    plt.title('Performance of Sorting Algorithms with Varying k Values')
    plt.xlabel('k (Threshold for switching to Insertion Sort)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the test
if __name__ == "__main__":
    test_sorts()
