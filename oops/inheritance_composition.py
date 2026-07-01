# Inheritance and Composition in Python

# class BaseChai:
    
#     def __init__(self, type_):
#         self.type = type_
        
        
#     def prepare(self):
#         print(f"Preparing {self.type} chai....")
        
        
# class MasalaChai(BaseChai):
    
#     def adding_spices(self):
#         print("Adding spices to the chai....")
        
        
        
# # dclaring composition class

# class ChaiShop:
#     chai_cls = BaseChai # class variable to hold the reference of BaseChai class,
    
#     def __init__(self):
#         self.chai = self.chai_cls("Masala")  # Creating an instance of BaseChai (or its subclass) and assigning it to the 'chai' attribute.
        
        
#     def serve_chai(self):
#         print("Serving chai....")
#         print(f"Chai Type: {self.chai.type}")
#         self.chai.prepare()  # Calling the 'prepare' method of the 'chai' instance.
        
        
# shop = ChaiShop()
# shop.serve_chai()  # Output: Serving chai.... Chai Type: Masala


# A composition is an oops concept where one class contains an object of another class as a member variable. It represents a "has-a" relationship between classes. In the above example, the ChaiShop class has an object of the BaseChai class (or its subclass) as a member variable, demonstrating composition.


class Engine:
    
    def start(self):
        print("Engine started.")
        
    def stop(self):
        print("Engine stopped.")
        
        
class Car:
    
    def __init__(self):
        self.engine = Engine() # Composition: Car has an Engine.
        
    def start_car(self):
        self.engine.start()  # Delegating the start action to the Engine object.
        print("Car is ready to go!")
        
        
    def stop_car(self):
        self.engine.stop()  # Delegating the stop action to the Engine object.
        print("Car has stopped.")
        

car = Car()
# car.start_car()  # Output: Engine started. Car is ready to go!
# car.stop_car()   # Output: Engine stopped. Car has stopped.
        
        
        
class CPU:
    
    def process(self):
        print("CPU is processing data.")
        
class RAM:
    
    def load(self):
        print("RAM is loading data.")
        
class HardDrive:
    
    def read(self):
        print("Hard Drive is reading data.")
        
        
class Computer:
    def __init__(self):
        self.cpu = CPU()  # Composition: Computer has a CPU.
        self.ram = RAM()  # Composition: Computer has RAM.
        self.hard_drive = HardDrive()  # Composition: Computer has a Hard Drive.
        
        
pc = Computer()
pc.cpu.process()  # Output: CPU is processing data.
pc.ram.load()     # Output: RAM is loading data.
pc.hard_drive.read()  # Output: Hard Drive is reading data.        