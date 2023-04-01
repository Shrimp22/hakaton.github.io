from db.models import Users
from db.schemas import users
from fastapi import HTTPException
from sqlalchemy.orm import Session
from dependencies import pwd_context



def create_user(user: users.UserBase, db: Session):
    find_user = db.query(Users).filter(Users.email == user.email).one_or_none()
    if find_user is not None:
        raise HTTPException(400, "User with this email address already exist!")
    hashed_password = pwd_context.hash(user.password)
    insert = Users(
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        password=hashed_password,
        email = user.email
    )
    
    db.add(insert)
    db.commit()
    db.refresh()
    return insert


def login(db: Session, user: users.UserLogin):
    get_user = db.query(Users).filter(Users.email == user.email).first()
    
    if get_user is None:
        raise HTTPException(404, "User not found")
    if pwd_context.verify(user.password, get_user.password) == False:
        raise HTTPException(401, "Invalid password")
    return get_user