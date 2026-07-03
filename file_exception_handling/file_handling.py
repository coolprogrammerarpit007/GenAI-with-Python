# file handling and exception handling
file = open("orders.txt","w")
try:
    file.write("Masala Chai\n")
    file.write("Ginger Chai\n")
    file.write("Lemon Chai\n")
    file.write("Masala Dosa\n")
    
except IOError:
    print("Error: Unable to write to the file.")
    
else:
    print("Orders written to the file successfully.")
    
finally:
    file.close()
    print("File closed successfully.")
    
    
    
# modern way to handle file operations using 'with' statement, # which automatically takes care of closing the file after the block is executed.

# import os

# with open("orders.txt", "w") as file:
#     file.write("Masala Chai\n")
#     file.write("Ginger Chai\n")
#     file.write("Lemon Chai\n")
#     file.write("Masala Dosa\n")

# print("Current working directory:", os.getcwd())
# print("File saved at:", os.path.abspath("orders.txt"))
