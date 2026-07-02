# 3 ways to access base classes

# Code Duplication
# Explicit Call
# Super


class Chai:
    
    def __init__(self,type_,strength):
        self.type = type_
        self.strength = strength
        
        
class GingerChai(Chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_,strength)
        # Chai.__init__(self,type_,strength) # this is explicit call to base class
        self.spice_level = spice_level
        
        


# Method Resolution Order -> Multiple Inheritance

