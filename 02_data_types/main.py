# number = 12
# print(f"Identity of number: {id(number)}")
# number = 24
# print(f"Identity of number: {id(number)}")


# friends = set()

# friends.add("Alice")
# friends.add("Bob")
# friends.add("Charlie")
# print(f"Identity of friends set: {id(friends)}")
# print(f"Friends set: {friends}")


# # Numbers are immutable, so when we change the value of `number`, it creates a new object in memory, it means in case of number refrence changes so it points to a new object.
# # Sets are mutable, so when we add elements to the `friends` set, it modifies the existing object in memory, so the reference remains the same.


# is_boiling = True
# stri_count = 5
# total_actions = is_boiling + stri_count # This will result in 6 (True = 1, False = 0) as it is called upcasting, where the boolean value is converted to an integer for the addition operation.
# print(f"Total actions: {total_actions}") 


# # There are three logical operators in Python: `and`, `or`, and `not`. These operators are used to combine or invert boolean values.
# # And operator returns True if both operands are True, or False otherwise. The Or operator returns True if at least one of the operands is True, or False if both are False. The Not operator inverts the boolean value of its operand, returning True for False and False for True.
# # And operator has higher precedence than Or operator, so it is evaluated first in expressions that contain both operators. Parentheses can be used to group expressions and override the default precedence rules.
# # operators can be used in conditional statements, loops, and other control flow structures to make decisions based on boolean values.

# water_added = True
# heat_applied = False

# water_boiling = water_added and heat_applied
# print(f"Water boiling: {water_boiling}")  # Output: False


# # Strings are immutable sequences of characters in Python. They can be created using single quotes, double quotes, or triple quotes for multi-line strings. Strings support various operations such as concatenation, slicing, and formatting. They also have a wide range of built-in methods for manipulation and analysis.
# greeting = "Hello"  
# print(f"Greeting: {greeting}")  # Output: Hello
# print(f"Reversed Greeting: {greeting[::-1]}")  # Output: olleH


# label_text = "Temperature"
# print(f"Label text: {label_text}")  # Output: Temperature
# encoded_label = label_text.encode("utf-8")
# print(f"Encoded label: {encoded_label}")  # Output: b'Temperature'
# decoded_label = encoded_label.decode("utf-8")
# print(f"Decoded label: {decoded_label}")  # Output: Temperature

# # use case of encoding and decoding is when you need to store or transmit text data in a specific format, such as when sending data over a network or saving it to a file. Encoding converts the string into bytes, which can be easily transmitted or stored, while decoding converts the bytes back into a string for further processing or display.

# # Tuples and membership testing
# # Tuples are immutable sequences of elements in Python. They can contain elements of different data types and are defined using parentheses. Membership testing can be performed on tuples using the `in` and `not in` operators, which check if an element exists within the tuple.

# planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
# print(f"Planets: {planets}")  # Output: Planets: ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')

# for planet in planets:
#     if planet in ("Earth", "Mars"):
#         print(f"{planet} is a terrestrial planet.")  # Output: Earth is a terrestrial planet. Mars is a terrestrial planet.
#     else:
#         print(f"{planet} is a gas giant.")  # Output: Mercury is a gas giant. Venus is a gas giant. Jupiter is a gas giant. Saturn is a gas giant. Uranus is a gas giant. Neptune is a gas giant.
        
        
# friends_tuple = ("Alice", "Bob", "Charlie")
# friend1,friend2,friend3 = friends_tuple
# print(f"Friend 1: {friend1}")  # Output: Friend 1: Alice
# print(f"Friend 2: {friend2}")  # Output: Friend 2: Bob
# print(f"Friend 3: {friend3}")  # Output: Friend 3: Charlie


# # Lists and membership testing
# # Lists are mutable sequences of elements in Python. They can contain elements of different data types and are defined using square brackets. Membership testing can be performed on lists using the `in` and `not in` operators, which check if an element exists within the list.


# numbers_list = [1, 2, 3, 4, 5]
# print(f"Numbers list: {numbers_list}")  # Output: Numbers list: [1

# numbers_list.append(6)
# numbers_list.remove(2)
# numbers_list.sort(reverse=True)
# numbers_list.insert(2, 10)
# print(f"Modified numbers list: {numbers_list}")  # Output: Modified numbers list:


# cricket_players = ["Sachin Tendulkar", "Virat Kohli", "MS Dhoni", "Ricky Ponting"]
# tennis_players = ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Serena Williams"]
# football_players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr.", "Kylian Mbappé"]
# kabbadi_players = ["Pardeep Narwal", "Rahul Chaudhari", "Manjeet Chhillar", "Ajay Thakur"]
# all_players = cricket_players + tennis_players + football_players + kabbadi_players
# print(f"All players: {all_players}")  # Output: All players: ['Sach
# all_atheletes = []
# all_atheletes.extend(cricket_players)
# all_atheletes.extend(tennis_players)
# all_atheletes.extend(football_players)
# all_atheletes.extend(kabbadi_players)
# print(f"All atheletes: {all_atheletes}")  # Output: All athe


# # Operator overloading is a feature in Python that allows operators to have different meanings based on the context in which they are used. This means that the same operator can perform different operations depending on the data types of the operands involved. For example, the `+` operator can be used for both numerical addition and string concatenation, depending on whether the operands are numbers or strings. Operator overloading enhances code readability and allows for more intuitive use of operators with custom classes.

# # byte arrays and memoryview
# # use case of byte arrays and memoryview is when you need to manipulate binary data, such as reading from or writing to files, working with network protocols, or performing low-level data processing. Byte arrays provide a mutable sequence of bytes, while memoryview allows for efficient access and manipulation of the underlying buffer without copying the data.