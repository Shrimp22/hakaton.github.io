from fastapi import APIRouter, Depends
from dependencies import get_db
from db.schemas import users as user_schema
from db.crud import users
from dependencies import Settings
from fastapi_jwt_auth import AuthJWT


@AuthJWT.load_config
def get_config():
    return Settings()


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post('/', response_model=user_schema.UserBase)
def create_user_rotue(user: user_schema.UserBase, db=Depends(get_db)):
    return users.create_user(user, db)


@router.post('/login')
def user_login_route(user: user_schema.UserLogin, Authorize: AuthJWT = Depends(), db=Depends(get_db)):
    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)

    return users.login(db, user).id



@router.delete('/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    Authorize.unset_jwt_cookies()
    return {"detail": "Logged out"}

# TODO: email, password update