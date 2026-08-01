from datetime import datetime
from pydantic import BaseModel,ValidationError



class User(BaseModel):
    uid:int
    
    username:str
    email:str
    
    verified_at:str|None = None
    
    bio:str = ""
    is_active:bool = True
    
    
    full_name:str | None = None   # it says that fullname can be either string or None
    
    
# By default validation not work on assignment, to change default behavior need to work in model configuration


try:    
    user = User(uid=123 , username="Arpit007",email="arpit@gmail.com")
    user.bio = "Python Developer"
    
    # to convert our model to dictionary

    # data serialization:- model_dump and model_dump_json is a effective method to serialize model data and to send it over a network request or save it to a file. serialize means convert your data into a simple format which can be easily save or send over external file over an network request.

    print(user.model_dump()) 

    # to convert model into json string

    print(user.model_dump_json(indent=2))
    print(user)
    # print(user.username)
    
except ValidationError as e:
    print(e)

