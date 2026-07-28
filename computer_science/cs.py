# GIL In Python
# Global Interpreter Lock (GIL) is a mutex (lock) in the standard CPython implementation that allows only one thread to execute Python bytecode at a time. This means that even on a multi-core processor, a multi-threaded Python program will only utilize a single CPU core for CPU-bound tasks.

# Why Python Has the GILThread Safety: It protects CPython's memory management from race conditions.Reference Counting: Python uses reference counting for garbage collection, which requires safe tracking across threads.C Extensions: It simplifies the integration of non-thread-safe C libraries.

# Impact on PerformanceCPU-Bound Tasks: Multithreading will not speed up heavy computations (like data processing or math). In fact, thread management overhead might make it slower.I/O-Bound Tasks: Multithreading works excellently for tasks waiting on external resources (like network requests, file reading, or database queries) because the GIL is released during I/O operations.


import threading
import time


def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    
    for _ in range(100_000_000):
        count += 1
        
    print(f"{threading.current_thread().name} completed brewing...")
    
    
t1 = threading.Thread(target=brew_chai,name="Barista-1")
t2 = threading.Thread(target=brew_chai,name="Barista-2")


start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()


print(f"Total Time Taken: {end-start:.2f} seconds")