# Threads and Lock State in Python

import threading
import time


def boil_milk():
    print("Boiling Milk....")
    time.sleep(2)
    print(f"Milk Boiled....")
    
    
def toast_burn():
    print(f"Toasting Burn.....")
    time.sleep(2)
    print(f"Done with burning toast...")
    
    
    
# start = time.time()
    
# t1 = threading.Thread(target=boil_milk)
# t2 = threading.Thread(target=toast_burn)


# t1.start()
# t2.start()


# t1.join()
# t2.join()


# end = time.time()


# print(f"Breakfast is ready in: {end-start:.2f} seconds")








counter = 0

lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
            
            
            
threads = [threading.Thread(target=increment) for _ in range(10)]
[ t.start() for t in threads]
[ t.join() for t in threads]



print(f"Final COunter: {counter}")