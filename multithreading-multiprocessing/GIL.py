# GIL In Python
# GIL stands for Global Interpreter Lock. It is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This means that even in a multi-threaded Python program, only one thread can execute Python code at a time.

# mutex is a memory lock means whoever thread touches memory first it has full control and locks for another thread.
# GIL uses that mutex.

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started  brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")
    
    
thread1 = threading.Thread(target=brew_chai,name="Barista1")
thread2 = threading.Thread(target=brew_chai,name="Barista2")


start = time.time()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()

total_time = end-start

print(f"Total Time Taken: {total_time:.2f} seconds.")