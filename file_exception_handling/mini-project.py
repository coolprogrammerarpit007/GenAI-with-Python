class InvalidChaiError(Exception): pass

def order_bill(flavor,cups):
    menu = {"Ginger Chai": 30, "Masala Chai": 25, "Lemon Chai": 20}
    
    try:
    
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} is not available in the menu.")
        
        
        if not isinstance(cups,int) or cups <= 0:
            raise ValueError("Number of cups must be a positive integer.")
        
        total_cost = menu[flavor] * cups
        print(f"Total cost for {cups} cup(s) of {flavor} is: {total_cost}")
        
    except InvalidChaiError as ice:
        print(f"Error: {ice}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
        
    else:
        print("Order processed successfully.")
        
    finally:
        print("Thank you for visiting our restaurant.")
        
order_bill("Masala Chai", 3)  # Valid order
order_bill("Green Tea", 2)    # Invalid flavor
order_bill("Ginger Chai", 0)  # Invalid number of cups
order_bill("Lemon Chai", "two")   # Invalid number of cups