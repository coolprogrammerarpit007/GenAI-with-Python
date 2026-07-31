# Mixing Threads with asyncio in python


import asyncio
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

# def check_stock(item):
#     print(f"Checking {item} in the stock...")
#     time.sleep(3) # Blocking Operation
#     return f"{item} stock: 42"


# async def main():
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool,check_stock,"Black Tea")
        # print(result)
        
        
        
# asyncio.run(main())



# Mixing MultiProcess with Asyncio

def encrypt(data):
    return f"🔒🔑 {data[::-1]}"


async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,encrypt,"credit_card_1234")
        print(result)
        
        
        
if __name__ == "__main__":
    asyncio.run(main())
