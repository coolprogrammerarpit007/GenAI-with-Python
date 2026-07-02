class A:
    label = "A: Base Class"
    
    
class B(A):
    label = "B: Masala Class"
    
    
class C(A):
    label = "C: Herbal Blend Class"
    
    
class D(B,C):
    pass


cup = D()
# print(cup.label)



# Static and class Methods 



class ChaiUtils:
    
    @staticmethod
    def clean_ingredents(text):
        return [item.strip() for item in text.split(",")]
    
    
raw = " WATER  , MILK , GINGER , LEMON , HONEY"

obj = ChaiUtils()
result = ChaiUtils.clean_ingredents(raw)
# print(result)


# class Methods

class ChaiOrder:
    
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size= size
        
        
    @classmethod
    def form_dict(cls,order_data):
        return cls(order_data["tea_type"],order_data["sweetness"],order_data["size"])
    
    
order1 = ChaiOrder.form_dict({"tea_type":"Black Tea","sweetness":"Mild Sugar","size":"Medium"})
print(order1)