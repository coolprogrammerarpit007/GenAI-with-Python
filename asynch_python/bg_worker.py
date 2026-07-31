import time
import threading
import asyncio


def background_worker():
    index = 0
    while index<=5:
        index += 1
        time.sleep(1)
        print("Logging The System Health...")
        
        
async def fetch_orders():
    await asyncio.sleep(3)
    print(f"🎁🎁 order fetched")
    
    
thread = threading.Thread(target=background_worker,daemon=True)
thread.start()
thread.join()


asyncio.run(fetch_orders())