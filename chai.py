class Chai:
    
    def __init__(self,sweetness,milk_level,spice_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
        self.spice_level = spice_level
        
        
    def add_milk(self,amount):
        self.milk_level += amount
        print(f"Added {amount} units of milk. New milk level: {self.milk_level}")
        
        
    def add_spice(self,spice_amount):
        self.spice_level += spice_amount
        print(f"Added {spice_amount} units of spice. New spice level: {self.spice_level}")
        
    def get_spice_milk_levels(self):
        return self.spice_level, self.milk_level
    
    
chai = Chai(sweetness=5, milk_level=3, spice_level=2)

print(f"Initial spice level: {chai.spice_level}, Initial milk level: {chai.milk_level}")