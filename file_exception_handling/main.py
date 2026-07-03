# File and Exception Handling in Python

# Types of Error
# IndexError: Raised when an index is out of range.
# KeyError: Raised when a key is not found in a dictionary.
# ValueError: Raised when a function receives an argument of correct type but inappropriate value.
# ZeroDivisionError: Raised when a division by zero is performed.
# FileNotFoundError: Raised when trying to open a file that does not exist.
## Exception Handling
# try: This block of code will be executed and if an exception occurs, it will be caught by the except block.

# orders = ["Masla Dosa", "Idli", "Vada", "Pongal"]

# try:
#     order_number = int(input("Enter the order number (0-3): "))
#     print("You Ordered: ", orders[order_number])
    
# except IndexError:
#     print("Error: Order number is out of range. Please enter a number between 0 and 3.")
    
# except ValueError:
#     print("Error: Invalid input. Please enter a valid Order Number.")
    
    
# else:
#     print("Thank you for your order!")
    
# finally:
#     print("Next order will be taken shortly.")


# catching multiple exceptions


# def process_order(item,qty):
#     try:
#         price = {"masala": 20}[item]
#         cost = price * qty
#         print(f"Total cost for {qty} {item}(s) is: {cost}")
        
#     except KeyError:
#         print(f"Error: {item} is not available in the menu.")
        
#     except TypeError:
#         print("Error: Quantity must be a number.")
        
#     else:
#         print("Order processed successfully.")
        
#     finally:
#         print("Thank you for visiting our restaurant.")
        
        
# process_order("masala", 2)  # Valid order
# process_order("idli", 3)    # Invalid item
# process_order("masala", "three")  # Invalid quantity


# raise your own exception

# def validate_marmaid_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     elif age > 35:
#         raise ValueError("Age cannot be greater than 35.")
    
#     return True

# try:
#     age = int(input("Enter the age of the mermaid: "))
#     validate_marmaid_age(age)
#     print("Valid age for a mermaid.")
    
# except ValueError as ve:
#     print(f"Error: {ve}")
    
# else:
#     print("Age validation successful.")
    
# finally:
#     print("Age validation completed.")


# custom Exception