number = 12
print(f"Identity of number: {id(number)}")
number = 24
print(f"Identity of number: {id(number)}")


friends = set()

friends.add("Alice")
friends.add("Bob")
friends.add("Charlie")
print(f"Identity of friends set: {id(friends)}")
print(f"Friends set: {friends}")


# Numbers are immutable, so when we change the value of `number`, it creates a new object in memory, it means in case of number refrence changes so it points to a new object.
# Sets are mutable, so when we add elements to the `friends` set, it modifies the existing object in memory, so the reference remains the same.


is_boiling = True
stri_count = 5
total_actions = is_boiling + stri_count # This will result in 6 (True = 1, False = 0) as it is called upcasting, where the boolean value is converted to an integer for the addition operation.
print(f"Total actions: {total_actions}") 


# There are three logical operators in Python: `and`, `or`, and `not`. These operators are used to combine or invert boolean values.
# And operator returns True if both operands are True, or False otherwise. The Or operator returns True if at least one of the operands is True, or False if both are False. The Not operator inverts the boolean value of its operand, returning True for False and False for True.
# And operator has higher precedence than Or operator, so it is evaluated first in expressions that contain both operators. Parentheses can be used to group expressions and override the default precedence rules.
# operators can be used in conditional statements, loops, and other control flow structures to make decisions based on boolean values.

water_added = True
heat_applied = False

water_boiling = water_added and heat_applied
print(f"Water boiling: {water_boiling}")  # Output: False