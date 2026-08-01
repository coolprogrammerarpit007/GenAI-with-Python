from datetime import datetime,UTC
from functools import partial
from typing import Literal,Annotated
from uuid import UUID,uuid4
from pydantic import BaseModel,Field,EmailStr,HttpUrl,SecretStr,ValidationError


class BlogPost(BaseModel):
    uid:UUID = Field(default_factory=uuid4)
    title:Annotated[str,Field(min_length=3,max_length=20)] # Annotated are used to add data type constraints
    email:EmailStr
    website: HttpUrl | None = None
    blog_access_hint: SecretStr
    content:Annotated[str,Field(min_length=20)]
    author_id: str | int 
    
    
    view_count:int = 0
    is_published:bool = False
    
    tags:list[str] = Field(default_factory=list)
    
    # created_at: datetime = Field(default_factory=lambda:datetime.now(tz=UTC))
    created_at: datetime = Field(default_factory=partial(datetime.now,tz=UTC))
    
    
    status:Literal["draft","published","archived"] = "draft"
    
    slug:Annotated[str,Field(pattern=r"^[a-z0-9-]+$")]
    
    
    
post = BlogPost(
    title="Getting",
    email="arpit@gmail.com",
    website="https://www.google.com/",
    blog_access_hint="secret123",
    content="Here's how to begin... Getting Started with Python, Let's begin our work and start",
    author_id="12345",
    slug="blog"
)


print(post)