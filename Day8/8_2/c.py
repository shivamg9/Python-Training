"""
c. Analyzing time taken, CPU usage, and memory usage:
"""

import time
import psutil
import threading
from memory_profiler import profile

# ... (factorial_with_delay and calculate_factorials functions are the same as before)
def factorial_with_delay(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
        time.sleep(0.001)
    return result



def calculate_factorial_thread(number, result_list):
    result = factorial_with_delay(number)
    result_list.append(result)

# def calculate_factorials_with_multithreading(numbers):
#     results = []
#     threads = []

#     for num in numbers:
#         thread = threading.Thread(target=calculate_factorial_thread, args=(num, results))
#         thread.start()
#         threads.append(thread)
    
#     for thread in threads:
#         thread.join()
    
#     return results



@profile
def calculate_factorials(numbers):
    results = []
    for num in numbers:
        result = factorial_with_delay(num)
        results.append(result)
    return results
@profile
def calculate_factorials_with_multithreading(numbers):
    results = []
    threads = []

    for num in numbers:
        thread = threading.Thread(target=calculate_factorial_thread, args=(num, results))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return results


if __name__ == "__main__":
    numbers_list = [5, 7, 3, 10, 4]

    print("Analyzing factorials without multithreading:")
    start_time = time.time()
    results = calculate_factorials(numbers_list)
    end_time = time.time()
    print("Factorials without multithreading:", results)
    print("Time taken (without multithreading):", end_time - start_time, "seconds")
    print("CPU Usage (without multithreading):", psutil.cpu_percent(), "%")
    print("Memory Usage (without multithreading):", psutil.virtual_memory().used / (1024 * 1024), "MB")

    print("\nAnalyzing factorials using multithreading:")
    start_time = time.time()
    results = calculate_factorials_with_multithreading(numbers_list)
    end_time = time.time()
    print("Factorials using multithreading:", results)
    print("Time taken (using multithreading):", end_time - start_time, "seconds")
    print("CPU Usage (using multithreading):", psutil.cpu_percent(), "%")
    print("Memory Usage (using multithreading):", psutil.virtual_memory().used / (1024 * 1024), "MB")

