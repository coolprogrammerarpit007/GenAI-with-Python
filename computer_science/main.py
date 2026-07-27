# Concurrency and Parallelism

# concurrency:- doing multiple tasks at same time. in a single core with multi-threads in single core
# Parallelism:- doing multiple tasks at same time in multiple cores of cpu

# in case of concurrency-> whatever task got completed you return but in case of multiprocessing all tasks once need to be completed then only final combined result will return. 

import threading
import time


def take_orders():
    for i in range(1,4):
        print(f"Taking Order for #{i} person")
        time.sleep(2)
        
        
        
def brewing_chai():
    for i in range(1,4):
        print(f"Brewing Chai for #{i} person")
        time.sleep(3)
        
        
        
        
# creating threads


t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=brewing_chai)


# # starting threads
# t1.start()
# t2.start()

# # wait for both to finish

# t1.join()
# t2.join()



# print("All orders are taken and Chai Brewed...")



# Multiprocessing

from multiprocessing import Process
import time


def brew_chai(chai_name):
    print(f" Start of {chai_name} Brewing")
    time.sleep(3)
    print(f"End of {chai_name} chai Brewing")
    
    
    
    
if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai,args=(f"Chai Maker #{i+1}",))
        for i in range(3)
    ]
    
    
    # start all process then wait all to complete
    
    for p in chai_makers:
        p.start()
        
        
    # wait for all process to complete
    for p in chai_makers:
        p.join()
        
        
    print("All chai served")
    
