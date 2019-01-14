from multiprocessing.dummy import Pool as ThreadPool
import time

def my_function(item):
    b = item[0]*item[1]
    time.sleep(2)
    return b

def without_threading(my_array):
    results = []
    start = time.time()

    for item in my_array:
        print(item)
        results.append(my_function(item))

    print(results)
    print("Execution time = {0:.5f}".format(time.time() - start))

def with_threading(my_array):
    results = []
    start = time.time()
    pool = ThreadPool(24)
    results = pool.map(my_function, my_array)
    print(results)
    print("Execution time = {0:.5f}".format(time.time() - start))

my_array = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9],[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
print("########")
without_threading(my_array)
print("########")
print("########")
print("########")
with_threading(my_array)
print("########")
