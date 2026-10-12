from pydantic import BaseModel, Field, EmailStr, model_validator, field_validator, computed_field
from typing import Annotated, Optional

# class Address(BaseModel):
#         city :Annotated[str, Field(min_length=2, description="city must be at least 2")]
#         country: Annotated[str, Field(min_length=2, description="country must be at least 2")]
#         postal_code: Optional[str] = Field(default=None)

# class User(BaseModel):
#     username:Annotated[str, Field(min_length=3, max_length=30, description="username must be at least of 3 chars and max 30 chars")]
#     email:str
#     age:Annotated[int, Field(ge=13, le=100, description="username must be at least of 3 chars and max 30 chars")]
#     skills:list[str] = []
#     address: Address



# user = User(
#     username="huzefah",
#     email="Huzefa@gmail.com",
#     age=21,
#     skills=["Python", "Pydantic"],
#     address={
#         "city": "Multan",
#         "country": "Pakistan",
#         "postal_code": "60000"
#     }
# )
# print(user.model_dump_json())



class Registration(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=20, description="user name must be between 3 to 20 chars")]
    email: str
    password: Annotated[str, Field(min_length=8, description="user must set its password with at least 8 chars")]
    confirm_password : str
    age: Annotated[int, Field(ge=13, le=100, description="age must be between 13 to 100")]

    @model_validator(mode="after")
    def passwordChecker(self):
        if self.password != self.confirm_password:
            raise ValueError("Password didn't match")
        return self
    
    @field_validator("username")
    def user(v):
        return v.strip()
    
    @computed_field(return_type=str)
    @property
    def full_name(self):
        return f"{self.username} javed"


data = {
    "username": "  Huzefah  ",
    "email": "huzefah@gmail.com",
    "password": "Python@123",
    "confirm_password": "Python@123",
    "age": 21
}
r = Registration(**data)
    
print(r.model_dump_json())       