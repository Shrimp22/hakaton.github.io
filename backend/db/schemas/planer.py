from pydantic import BaseModel
from datetime import datetime
from users import User
class PlanerBase(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    
    class Config:
        orm_mode=True
        
        
class ListPlaners(PlanerBase):
    user: User
    
    class Config:
        orm_mode=True