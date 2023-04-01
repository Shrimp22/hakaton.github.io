from pydantic import BaseModel
from datetime import datetime

class PlanerBase(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    
    class Config:
        orm_mode=True