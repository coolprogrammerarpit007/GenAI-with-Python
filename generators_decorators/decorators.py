from functools import wraps

# # decorators in python
# def my_decorator(func):
    
#     @wraps(func)
#     def wrapper(name):  # -> it preserve the metadata,name of function
#         print("Before calling our function...")
#         func(name)
#         print("After calling our function...")
        
#     return wrapper


# @my_decorator

# def greet_user(name):
#     print(f"Nice to meet you {name}")
    
# greet_user("Arpit Mishra")
# print(greet_user.__name__)


# Build a logger with decorator


# def log_activity(func):
#     @wraps(func)
    
#     def wrapper(*args,**kwargs):
#         print(f"Calling {func.__name__}")
#         result = func(*args,**kwargs)
#         print(f"Finished Calling {func.__name__}")
#         return result
    
#     return wrapper


# @log_activity

# def blue_chai(type):
#     print(f"Brewing {type} chai")
    
    
# blue_chai("Masala")



# Build An Authorizaton decorator

# def require_admin(func):
#     @wraps(func)
    
#     def wrapper(userrole):
#         print("Before calling: ",func.__name__)
        
#         if userrole != "admin":
#             print("Access denied, Admin Only....")
            
#         else:
#             # return func(userrole)
#             func(userrole)
        
        
#         print("After calling: ",func.__name__)
        
#     return wrapper


# @require_admin

# def access_tea_inventory(role):
#     print("Access granted to Inventory!!")
    
# access_tea_inventory('admin')