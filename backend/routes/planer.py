from fastapi import APIRouter, Depends
from dependencies import get_db, jwt_required
from db.schemas import planer as planer_schema
from db.crud import planer as planer_crud
from db.schemas import users as user_schema
from typing import List



router = APIRouter(
    prefix="/planer",
    tags=["planer"],
)


@router.post('/', response_model=planer_schema.PlanerBase)
def create_planer_route(planer: planer_schema.PlanerBase, user: user_schema.User = Depends(jwt_required),  db=Depends(get_db)):
    print(user)    
    return planer_crud.create_planer(db, planer, user.id)

@router.get('/', response_model=List[planer_schema.ListPlaners])
def list_planers_route(user: user_schema.User = Depends(jwt_required),  db=Depends(get_db)):
    print(user)
    
    return planer_crud.list_all_planers(db)