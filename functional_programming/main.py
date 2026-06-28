


# customer_name = input("Enter your name: ").capitalize()
# chai_type = input("Enter the type of chai you want (e.g., Masala, Green, Black): ").capitalize()


# def print_order_summary(name, chai):
#     print(f"\nThank you, {name}!, you have ordered a cup of {chai} chai. your order will be arrived in 5 minutes. Enjoy your drink!")
    
    
# print_order_summary(customer_name, chai_type)





# def fetch_sales(sales):
#     print("Fetching total sales of the month.....")
#     print(f"Total Sales in the month for the cafe are: {sales}")
#     print("*********** Fetching Complete for Sales ********************")
#     return sales
    
    
# def fetch_orders(orders):
#     print("Fetching total orders in this month for the cafe.....")
#     print(f"Total Orders in the month for the cafe are: {orders}")
#     print("*********** Fetching Complete for Orders ********************")
#     return orders
    


# def summarize_data():
#     print("Summarizing Sales Data..........")
#     total_sales = int(input("Enter Total Sales of the cafe this month: "))
#     total_orders = int(input("Enter total orders this month to the cafe: "))
#     total_monthly_sales,total_monthly_orders = fetch_sales(total_sales),fetch_orders(total_orders)
#     print("************ Total Month Summary *******************")
#     print(f"Total Sales in The Month Are: {total_monthly_sales} Against Total Orders in The Month: {total_monthly_orders}")
    
    
# def generate_report():
#     summarize_data()
    
    
# generate_report()


# def get_input():
#     name = input("Enter UserName: ").capitalize()
#     password = input("Enter User Password: ")
    
#     return name,password


# def validating_user(name,password):
#     if name != "" and len(password) > 4:
#         return True
    
#     return False


# def save_user(name):
#     print(f"Saving User: {name} into the database......")
    
    
# def register_user():
#     name,password = get_input()
#     valid_user = validating_user(name,password)
    
#     if valid_user:
#         save_user(name)
        
#     else:
#         print(f"User is Not Valid Username........")
        
        
        
# register_user()




# def calculate_bills(cups,price_per_cups):
#     return cups * price_per_cups


# total_bill = calculate_bills(5,10)
# print(f"Total Bill: {total_bill}")


# Scopes in functions

# Local -> Inside a function
# Enclosing from outer function if nested
# Global -> Top Level
# Built In


# NonLocal and global


# def update_order():
#     chai_type = "Eliachi"
    
#     def kitchen():
#         nonlocal chai_type
#         chai_type = "Ginger"
        
#     kitchen()
    
#     print(f"Chai Type: {chai_type}")
    
    
# update_order()


# Handling Arguments in func

# chai = "Ginger Tea"

# def prepare_chai(order):
#     print("Preparing...",order)
    
    
# prepare_chai(chai)


# Positional and Keyword Arguments

# *args and **kwargs in python


# Lambdas and Pure vs Non Pure functions

# Types of functions
# Pure vs Impure
# Recursive
# Anonmous/Lambda functions

# num = int(input("Enter Number: "))
# double = lambda num:num ** 2

# print(f"Square of Number: {num} is {double(num)}")
# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# multiply_result = lambda num1,num2:num1*num2

# print(f" Multiplication of Numbers {num1} and {num2} are: {multiply_result(num1,num2)}")


# Recusive Function

# def pour_chai(n):
#     if n == 0:
#         return "All Cups are Poured: "
    
#     print(f"CUP POURED: {n}")
#     return pour_chai(n-1)

# print(pour_chai(10))


# Documenting your functions

# chai_types = ["black","ginger","black","kadak"]

# black_tea = list(filter(lambda chai:chai == "black",chai_types))
# print(black_tea)

# def chai_flavor(flavor):
#     """ Return The Flavor """
#     return flavor

# print(chai_flavor.__doc__)


# imports Modules and functions in python

