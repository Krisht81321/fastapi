from fastapi import Depends, HTTPException, APIRouter, status
from blog import models, schemas
from blog.database import get_db
from blog.hashing import Hash
from sqlalchemy.orm import Session
from blog.repository import user

router=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_user(id, db)