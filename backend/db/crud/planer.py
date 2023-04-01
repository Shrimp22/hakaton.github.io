from db.models import Planer
from db.schemas import planer
from fastapi import HTTPException
from sqlalchemy.orm import Session


def create_planer(db: Session, planer: planer.PlanerBase, user_id: int):
    
    find_planer = db.query(Planer).filter(Planer.name == planer.name).one_or_none()
    if find_planer is not None:
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

def remove_planer(db: Session, planer_id: int):
    planer = db.query(Planer).filter(Planer.id == planer_id).delete()
    db.commit()
    return True


def get_planer_by_id(db: Session, planer_id: int):
    planer = db.query(Planer).filter(Planer.id == planer_id).first()
    return planer

def update_planer(db: Session, planer_id: int, planer_model: planer.PlanerBase):
    planer =  get_planer_by_id(db, planer_id)
    
    for key, val in planer_model.dict(exclude_unset=True).items():
        setattr(planer, key, val)
    
    
    
    db.add(planer)
    db.commit()
    db.refresh(planer)
    
    return planer