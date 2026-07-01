class Student:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        
        
    def introduce_student(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my roll number is {self.roll_no}.")
        
        
student1 = Student("Alice", 20, "A001")
student2 = Student("Bob", 22, "B002")
student3 = Student("Charlie", 21, "C003")
# student1.introduce_student()
# student2.introduce_student()
# student3.introduce_student()


# Attribute Shadowing

# Attribute shadowing occurs when an instance variable in a subclass has the same name as an instance variable in its superclass. In such cases, the subclass's instance variable "shadows" or overrides the superclass's instance variable.

class Chai:
    
    # These are class variables, shared by all instances of the class.
    temperature = "hot"
    strength = "strong"
    
    
cutting = Chai()
cutting.temperature = "cold"  # This creates an instance variable 'temperature' in the 'cutting' object, shadowing the class variable.
cutting.size = "medium"  # This creates an instance variable 'size' in the 'cutting' object.

# print(cutting.temperature)  # Output: cold (instance variable)
# print(Chai.temperature)     # Output: hot (class variable)
# del cutting.temperature  # Deleting the instance variable 'temperature' from the 'cutting' object.
# print(Chai.temperature)     # Output: hot (class variable)
# print(cutting.temperature)  # Output: hot (class variable, since the instance variable was deleted)
# print(cutting.size)         # Output: medium (instance variable)
# del cutting.size  # Deleting the instance variable 'size' from the 'cutting' object.
# print(hasattr(cutting, 'size'))  # Output: False (instance variable 'size' no longer exists)