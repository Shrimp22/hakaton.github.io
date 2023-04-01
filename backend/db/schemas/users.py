from pydantic import BaseModel

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    
    class Config:
        orm_mode=True
    
class UserBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str
    
    class Config:
        orm_mode=True
        

class UserLogin(BaseModel):
    email: str
    password: str