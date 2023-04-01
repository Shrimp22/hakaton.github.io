from fastapi import APIRouter, Depends
from dependencies import get_db
from db.schemas import users as user_schema
from db.crud import users
router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post('/', response_model=user_schema.UserBase)
def create_user_rotue(user: user_schema.UserBase, db = Depends(get_db)):
    return users.create_user(user, db)