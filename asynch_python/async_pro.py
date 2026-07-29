import asyncio
import time

async def brew(name):
    print(f"Brewing Chai: {name}...")
    await asyncio.sleep(5)  # await means wait for execution of coroutine in a non-blocking way
    print(f"Chai {name} is ready to be serve!.")
    
    
    
async def main():
    await asyncio.gather(
        brew("Massala Chai"),
        brew("Green Tea"),
        brew("Black Tea"),
        brew("Ice Tea"),
        brew("Ginger Tea")
        )
    
    
start = time.time()
asyncio.run(main())
end = time.time()


print(f"Total Time Taken for Brewing and Making Chai: {end-start:.2f}")