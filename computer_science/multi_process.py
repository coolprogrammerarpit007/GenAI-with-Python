from multiprocessing import Process
import threading
import time


def cpu_heavy():
    print(f"Crunching Some Numbers......")
    total = 0
    for i in range(10**7):
        total += i
        
    print(f"Total Done: {total}",total)
    
    
start = time.time()


#  ********************** Dealing CPU Heavy tasks with threading ***************************

# threads = [ threading.Thread(target=cpu_heavy) for _ in range(2)]

# [ t.start() for t in threads]
# [ t.join() for t in threads]


# ********************** End of CPU Heavy tasks handling with Thread **********************

# ************* Handling CPU Heavy task with unoptimized multiprocessing *******************

if __name__ == "__main__":
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]



# ******************************************************************************************

end = time.time()

print(f"Total Time Taken In Seconds: {end-start:.2f} seconds")