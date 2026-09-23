from pydantic import BaseModel, Field

class User(BaseModel):
    age: int = Field(ge=0, le=90)

data = {"age":1} 
user = User(**data)

print(user)