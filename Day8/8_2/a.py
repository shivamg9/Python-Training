"""
Implement basic function for finding factorial of single number. 
(function must sleep or 0.001second after each iteration)

a. Take list of N numbers and find their factorial without using multithreading and
show after 	results of all numbers are ready. 
"""


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

if __name__ == "__main__":
    numbers_list = [5, 7, 3, 10, 4]
    
    start_time = time.time()
    results = calculate_factorials(numbers_list)
    end_time = time.time()

    print("Factorials without multithreading:", results)
    print("Time taken (without multithreading):", end_time - start_time, "seconds")
