from db.models import Planer
from db.schemas import planer
from fastapi import HTTPException
from sqlalchemy.orm import Session


def create_planer(db: Session, planer: planer.PlanerBase, user_id: int):
    
    find_planer = db.query(Planer).filter(Planer.name == planer.name).one_or_none()
    if find_planer is None:
        raise HTTPException(400, "Planer already exist")
    insert = Planer(
        name=planer.name,
        description=planer.description,
        start_date=planer.start_date,
        end_date=planer.end_date,
        user_id=user_id
    )

    
    db.add(insert)
    db.commit()
    db.refresh(insert)
    
    return insert


def list_all_planers(db: Session):
    planers = db.query(Planer).all()
    return planers