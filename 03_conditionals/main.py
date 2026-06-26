# kettle_boiled = False  # Change this to False to test the other condition

# if kettle_boiled:
#     print("You can make tea.")
# else:
#     print("You need to boil the kettle first.")
    
    
    
# food_snack = input("What snack do you want to eat? ").lower()

# if food_snack == "cookies" or food_snack == "samosa":
#     print("Yum! Enjoy your snack.")
# else:
#     print("Sorry, we don't have that snack available.")


# tea_cup = input("What type of tea do you want? ").lower()

# if tea_cup == "small":
#     print("Price for small tea: $2")
# elif tea_cup == "medium":
#     print("Price for medium tea: $3")
# elif tea_cup == "large":
#     print("Price for large tea: $4")
# else:
#     print("Sorry, we don't have that size available.")


# device_status = "Active" if input("Is the device active? (yes/no) ").lower() == "yes" else "Inactive"

# if device_status == "Active":
#     room_temperature = float(input("Enter the room temperature in Celsius: "))
#     if room_temperature > 35:
#         print("Warning: The room temperature is too high for the device to operate safely.")
#     else:
#         print("The device is operating normally.")
        
# else:
#     print("The device is inactive. Please activate it to check the temperature.")



# order_item = float(input("Enter the price of the item you want to order: $"))

# delivery_fees = 0 if order_item  >= 300 else 30
# print(f"Delivery fees: ${delivery_fees}")


seat_type = input("Enter the seat type (sleeper, AC, general,luxury): ").upper()

match seat_type:
    case "SLEEPER":
         print("You have selected a Sleeper seat. Enjoy your journey!")
    case "AC":
         print("You have selected an AC seat. Enjoy your journey!")
    case "GENERAL":
        print("You have selected a General seat. Enjoy your journey!")
    case "LUXURY":
        print("You have selected a Luxury seat. Enjoy your journey!")
    case _:
        print("Invalid seat type. Please select a valid option.")
        

    
    