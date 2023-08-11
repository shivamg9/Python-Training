""" 
b.Take list of N numbers and find their factorial using multithreading 
and  show after result of all number is ready. 
"""

import threading
import time

import time

def factorial_with_delay(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
        time.sleep(0.001)
    return result

def calculate_factorials(numbers):
    results = []
    for num in numbers:
        result = factorial_with_delay(num)
        results.append(result)
    return results



def calculate_factorial_thread(number, result_list):
    result = factorial_with_delay(number)
    result_list.append(result)

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

    start_time = time.time()
    results = calculate_factorials_with_multithreading(numbers_list)
    end_time = time.time()

    print("Factorials using multithreading:", results)
    print("Time taken (using multithreading):", end_time - start_time, "seconds")
