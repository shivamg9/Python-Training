"""
Implement basic function for finding n'th fibonacci number of series. (function must sleep for 0.001second after each iteration) 

a.Take list of N numbers and find respective fibonacci number without using multiprocessing 	and show after results of all numbers are ready. 

b.Take list of N numbers and find their respective fibonacci number using multiprocessing 	and show after results of all numbers are ready. 

c.Analyse time taken, cpu usage, memory usage 
"""



import time
import psutil
import multiprocessing

# Function to calculate the nth Fibonacci number with a sleep of 0.001 second after each iteration
def fibonacci_with_sleep(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_1, fib_2 = 0, 1
        for _ in range(2, n + 1):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            time.sleep(0.001)  # Sleep for 0.001 seconds after each iteration
        return fib_2

# Function to calculate the nth Fibonacci number without sleep (for comparison)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_1, fib_2 = 0, 1
        for _ in range(2, n + 1):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        return fib_2

# Function to calculate Fibonacci numbers for a list of N numbers without using multiprocessing
def calculate_fibonacci_without_multiprocessing(numbers):
    fibonacci_results = []
    for num in numbers:
        fibonacci_results.append(fibonacci_with_sleep(num))
    return fibonacci_results

# Function to calculate Fibonacci numbers for a list of N numbers using multiprocessing
def calculate_fibonacci_with_multiprocessing(numbers):
    with multiprocessing.Pool() as pool:
        fibonacci_results = pool.map(fibonacci_with_sleep, numbers)
    return fibonacci_results

if __name__ == "__main__":
    N = 10  # Number of Fibonacci numbers to calculate

    # Generate a list of N numbers
    numbers = list(range(1, N + 1))

    # Part a: Calculate Fibonacci numbers without multiprocessing and measure time, CPU usage, and memory usage
    start_time_a = time.time()
    fibonacci_results_a = calculate_fibonacci_without_multiprocessing(numbers)
    end_time_a = time.time()

    print("Fibonacci results without multiprocessing:")
    print(fibonacci_results_a)
    print(f"Time taken without multiprocessing: {end_time_a - start_time_a:.4f} seconds")
    print(f"CPU usage without multiprocessing: {psutil.cpu_percent()}%")
    print(f"Memory usage without multiprocessing: {psutil.virtual_memory().percent}%")

    # Part b: Calculate Fibonacci numbers with multiprocessing and measure time, CPU usage, and memory usage
    start_time_b = time.time()
    fibonacci_results_b = calculate_fibonacci_with_multiprocessing(numbers)
    end_time_b = time.time()

    print("\nFibonacci results with multiprocessing:")
    print(fibonacci_results_b)
    print(f"Time taken with multiprocessing: {end_time_b - start_time_b:.4f} seconds")
    print(f"CPU usage with multiprocessing: {psutil.cpu_percent()}%")
    print(f"Memory usage with multiprocessing: {psutil.virtual_memory().percent}%")
