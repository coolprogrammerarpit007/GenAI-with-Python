# Concurrency and parallelism in Python can be achieved using the `threading` and `multiprocessing` modules. Below is an example of how to use both modules to perform concurrent and parallel tasks.

# concurrency is achieved using threads, which allows multiple tasks to run seemingly at the same time within a single process. However, due to Python's Global Interpreter Lock (GIL), threads are not truly parallel and are best suited for I/O-bound tasks.

# concurrency is also achieved using asynchronous programming with the `asyncio` module, which allows for non-blocking I/O operations and can handle many tasks concurrently without the need for multiple threads or processes.

# Parallelism is achieved using processes, which allows multiple tasks to run in separate memory spaces and can take advantage of multiple CPU cores. This is suitable for CPU-bound tasks that require heavy computation.

# threading in Python is implemented using the `threading` module, which provides a way to create and manage threads. Each thread runs in the same memory space, which allows for shared data but also requires careful synchronization to avoid

# concurrency/MultiThreading 

import threading
import time

def take_orders():
    for i in range(1,4):
        print(f" Taking Order of customer {i}")
        time.sleep(2)
        
def prepare_food():
    for i in range(1,4):
        print(f" Preparing food for customer {i}")
        time.sleep(3)
        
        
order_thread = threading.Thread(target = take_orders)
food_thread = threading.Thread(target = prepare_food)

order_thread.start()
food_thread.start()


order_thread.join()
food_thread.join()