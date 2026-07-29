# Asynchronous Programming in Python

# async def -> declare a coroutine (special function that can be paused)
# await -> pauses execution until the result is ready
# asyncio -> built in library for python

# Event Loop -> This is an engine that runs and schedule coroutines in python

import asyncio

async def brew_chai():
    print("Brewing Chai...")
    await asyncio.sleep(2)
    print("Chai is ready.")
    
    
    
asyncio.run(brew_chai())

