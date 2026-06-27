
# for number in range(10):
#     print(f"Serving Chai to token #{number+1}")


# batch = int(input("Enter the number of batches: "))

# for batch_number in range(batch):
#     print(f"Serving Batch Number: {batch_number + 1}")


# tea_list = ["Masala Chai", "Ginger Chai", "Lemon Tea", "Green Tea", "Black Tea"]

# for tea in tea_list:
#     print(f"Order ready for: {tea}, please collect your order.")


# enumerate() function is used to get the index of the item in the list along with the item itself.
# sportsman_list = ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Jasprit Bumrah", "Hardik Pandya"]

# for number,sportsman in enumerate(sportsman_list):
#     print(f"SportsMan Number: {number + 1}, Name: {sportsman}")


# zip function is used to combine two or more lists into a single iterable object.

# customer_names = ["Alice", "Bob", "Charlie", "David"]
# order_bills = [250, 300, 150, 400]


# for person,bill in zip(customer_names,order_bills):
#     print(f"Order delivery for {person} is ready. Please collect your order. Your bill amount is: ${bill}")


# current_temperature = int(input("Enter the current temperature in Celsius: "))


# while current_temperature < 100:
#     print(f"Current temperature is {current_temperature}°C. Heating the water...")
#     current_temperature += 10
    
# print(f"Current temperature is {current_temperature}°C. Water has reached boiling point.")


# break,continue,pass statements are used to control the flow of loops in Python.
# break statement is used to exit the loop when a certain condition is met.
# continue statement is used to skip the current iteration and move to the next iteration of the loop
# pass statement is used as a placeholder for future code. It does nothing when executed.


# ice_cream_flovours = ["Vanilla", "Chocolate", "Strawberry", "Mango", "Pista"]
# user_choice = input("Enter your favourite ice cream flavour: ").capitalize()



# for flavour in ice_cream_flovours:
#     if flavour == user_choice:
#         print(f"Great choice! {flavour} is available.")
#         break
#     else:
#         continue
    
# else:
#     print(f"Sorry, {user_choice} is not available. Please choose from the available flavours: {', '.join(ice_cream_flovours)}.")


# walrus operator (:=) is used to assign a value to a variable as part of an expression. It allows you to both assign a value and use that value in the same expression.


# number = int(input("Enter a number to check if it is even or odd: "))

# if(result := number % 2 == 0):
#     print(f"{number} is an even number. {result}")
# else:
#     print(f"{number} is an odd number. {result}")


# requested_sizes = ["Small", "Medium", "Large", "Extra Large"]

# if(user_size := input("Enter Your Preferred Size: ")).capitalize() in requested_sizes:
#     print(f"Your preferred size {user_size} is available.")
# else:
#     print(f"Sorry, {user_size} is not available. Please choose from the available sizes: {', '.join(requested_sizes)}.")


# Iterate over a dictionary using for loop


users = [
    {"id":1,"total":100,"coupon":"P20"},
    {"id":2,"total":200,"coupon":"P30"},
    {"id":3,"total":300,"coupon":"P40"},
    {"id":4,"total":400,"coupon":"P50"},
]


discounts = {
    "P20": (0.2,0),
    "P30": (0.3,50),
    "P40": (0.4,100),
    "P50": (0.5,75)
}


for user in users:
    coupon = user["coupon"]
    userId = user["id"]
    userTotal = user["total"]
    percent,fixed_discount = discounts.get(coupon,(0,0))
    
    percent_discount = userTotal * percent
    total_discount = percent_discount + fixed_discount
    
    print(f"User ID: {userId}, Total Amount: ${userTotal}, Coupon: {coupon}, Percent Discount: ${percent_discount}, Fixed Discount: ${fixed_discount}, Total Discount: ${total_discount}")