from db.models import Planer
from db.schemas import planer
from fastapi import HTTPException
from sqlalchemy.orm import Session


def create_planer(db: Session, planer: planer.PlanerBase):
    insert = Planer(
        name=planer.name,
        description=planer.description,
        start_date=planer.start_date,
        end_date=planer.end_date
    )
    
    db.add(insert)
    db.commit()
    db.refresh()