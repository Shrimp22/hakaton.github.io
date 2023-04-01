from db.database import SessionLocal
from passlib.context import CryptContext

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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