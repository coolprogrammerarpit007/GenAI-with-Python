
# class OutOfIngredientsError(Exception):
#     """ Custom exception raised when the restaurant runs out of ingredients for a specific item.
    
#     """
    
#     pass

# def make_chai(milk,sugar):
#     try:
#         if milk < 1:
#             raise OutOfIngredientsError("Not enough milk to make chai.")
        
#         elif sugar < 1:
#             raise OutOfIngredientsError("Not enough sugar to make chai.")
        
#         print("Chai is preparing!")
        
#     except OutOfIngredientsError as e:
#         print(f"Error: {e}")
        
#     else:
#         print("Chai is ready to serve!")
        
#     finally:
#         print("Thank you for visiting our restaurant.")
        
        
# make_chai(0, 2)  # Not enough milk
# make_chai(2, 0)  # Not enough sugar
# make_chai(2, 2)  # Sufficient ingredients




