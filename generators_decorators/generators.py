# generators and decorators

# generators generate one value at time. they are memory efficient. not load everything in memory at once.
# instead of return keyword we use yield.
# generators are used cases where you not want all value at once , you wanted lazy loading!

# def serve_chai():
#     yield "Serving Ginger Tea!"
#     yield "Serving Black Tea!"
#     yield "Serving Elaichi Tea!"
    
    
# chai_cups = serve_chai() # => what it does is chai_cups is keeping reference to serve_chai so it not get value at once, once we loop through it value comes one at time.

# # yield pauses the function at one point and then resume the function where it paused.

# # print(chai_cups)

# for cup in chai_cups:
#     print(cup)



# def get_numbers():
#     """
#         returns number from range of 1 to 100 but one at time with memory efficiency.
#     """
#     for index in range(1,101):
#         yield index
        
        
# numbers = get_numbers()

# for number in numbers:
#     print(f"Number: {number}")


# Infinite generators in python

# def infinite_chai():
#     count = 1
#     while True:
#         yield f"Refill {count}"
#         count += 1
        
# refill = infinite_chai()

# for _ in range(3):
#     print(next(refill))
    
    # This will run infinite,never run it will crash system.
# for _ in refill:
#     print(next(refill))


# send value to generators

# def chai_customer():
#     print("What chai would you like to have? ")
#     order = yield
    
#     while True:
#         print(f"Your order is: {order}")
#         order = yield
        
        
# stall = chai_customer() # stor the reference of generator
# next(stall) # start the generator

# stall.send("Black Tea")
# stall.send("Lemon Tea")


# yield from and close the generators

# def local_chai():
#     yield "Masala Chai"
#     yield "Ginger  Chai"
    
    
# def imported_chai():
#     yield "Matcha"
#     yield "Oolang"
    
    
# def full_name():
#     yield from local_chai()
#     yield from imported_chai()
    
    
# all_chais = full_name()

# for chai in all_chais:
#     print(chai)
    
    
    
# def chai_stall():
#     try:
#         while True:
#             order = yield "Waiting for your order! "
            
#     except:
#         print(f"Stall Closed!, No more chai.......")
        
# stall = chai_stall()
# print(next(stall))
# stall.close() => good pratice and memory efficient for closing generator
    