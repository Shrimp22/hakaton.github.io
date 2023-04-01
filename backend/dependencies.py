from db.database import SessionLocal
from passlib.context import CryptContext
from pydantic import BaseModel

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Settings(BaseModel):
    authjwt_secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    authjwt_token_location = {'cookies'}
    authjwt_cookie_csrf_protect = False
    authjwt_access_token_expires = 3600
    # authjwt_refresh_token_expires = 15
    authjwt_cookie_max_age = 604800  # 1 week
    authjwt_cookie_secure = True
    authjwt_cookie_samesite = "none"

""" async def jwt_required(
        auth: AuthJWT = Depends(),
        db: Session = Depends(get_db)
):
    auth.jwt_required()

    email = auth.get_jwt_subject()
    user = db.query(models.User).filter(models.User.email == email).first()
    return user


async def jwt_optional(
        auth: AuthJWT = Depends(),
        db: Session = Depends(get_db)
):
    auth.jwt_optional()

    email = auth.get_jwt_subject()
    if email:
        user = db.query(models.User).filter(models.User.email == email).first()
        return user
    return None """