from pydantic import BaseModel


#  User Validation without the pydantic 
# def create_user(username,email,age):
#     if not isinstance(username,str):
#         raise TypeError("Username Must be string...")
    
#     if not isinstance(email,str):
#         raise TypeError("Invalid Email Format")
    
#     if not isinstance(age,int):
#         raise TypeError("Age must be an Integer...")
    
    
#     return {"username":username,"email":email,"age":age}






# Now validation using pydantic

class User(BaseModel):
    username:str
    email:str
    age:int
    
    

user1 = User(username="Arpit007",email="arpit.mishra.out@gmail.com",age=27)
# user2 = User(username=35,email="CoreyMShafer@gmail.com",age="38")


print(user1)
# print(user2)