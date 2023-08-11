"""
Implement simple function which takes name as input and returns "hello <name>" after 1 second. 
Do it for N names using multithreading and multiprocessing. 
"""

import threading
import time

def greet(name):
    time.sleep(1)
    print(f"Hello {name}")

def greet_using_multithreading(names):
    threads = []
    for name in names:
        thread = threading.Thread(target=greet, args=(name,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    names_list = ["Ram", "Shyam", "Sai", "Rahul", "Sia"]
    greet_using_multithreading(names_list)
