# daemon threads are the background threads which automatically exit when the main program got exited.

import threading
import time

def monitor_tea_temp():
    # Loop runs indefinitely in the background
    while True:
        print("Monitoring the tea temperature...")
        time.sleep(2)

# Create the background thread
t1 = threading.Thread(target=monitor_tea_temp, daemon=True)
t1.start()

# Keep main program alive for 5 seconds to see the thread work
print("Main Program Doing Work...")
time.sleep(5)

print("Main Program Done....")
