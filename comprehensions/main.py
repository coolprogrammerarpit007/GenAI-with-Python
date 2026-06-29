# List Comprehensions

prices = [10,20,30,40,50,60,70,80,90,100]

prices_doubles = [price * 2 for price in prices ]

# print(f"Original Prices: {prices}")
# print(f"Doubled  Prices: {prices_doubles}")

filtered_prices = [price for price in prices_doubles if price > 50]
# print(f"Prices greater than $50 are: {filtered_prices}")


# Set Comprehensions 

# { expression for item in itterable if condition }


favourite_chai = ["Masala Chai","Green Tea", "Masala Chai","Lemon Tea","Green Tea","Elaichi Chai"]

unique_chai = set(favourite_chai)
# print(unique_chai)


recipes = {
    "Masala Chai" : ["ginger","cardmom","clove"],
    "Elaichi Chai" : ["ginger","milk"],
    "Spicy Chai" : ["ginger","black pepper","clove"],
}


unique_spices = { spice for ingredients in recipes.values() for spice in ingredients}
# print(unique_spices)


# dictionary comprehensions

tea_price_inr = {
    "Masala Chai":48,
    "Green Tea":75,
    "Lemon Tea":200
}


tea_prices_usd = { tea:round(price/94.54) for tea,price in tea_price_inr.items() }

# print(tea_price_inr)
# print(tea_prices_usd)


# generators are used mainly for saving memory
# generator gives one item at time

# [x for x  in item ] -> this one stores all item once in memory
# (x for x  in item ) -> this one gives  item one at a time. it ives as we process data


# generator comprehensions 

# (expression for item in itterable if condition)


# daily_sales = [5,10,12,7,3,20,8,9,15]

# total_cups = (sale for sale in daily_sales if sale > 5)

# # generator provides method to whom which you provide itterable and it computes which is memory efficient operation.
# total_sales = sum(sale for sale in daily_sales if sale > 5)


# for cup in total_cups:
#     print(cup)

# print(total_sales)