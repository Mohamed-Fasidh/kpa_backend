from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(
    prefix="/api/forms",
    tags=["Wheel Specifications"]
)

@router.post("/wheel-specifications", response_model=schemas.WheelSpecificationOut)
def create_wheel_specification(
    spec: schemas.WheelSpecificationCreate,
    db: Session = Depends(get_db)
):
    return crud.create_wheel_specification(db, spec)

@router.get("/wheel-specifications", response_model=list[schemas.WheelSpecificationOut])
def get_wheel_specifications(db: Session = Depends(get_db)):
    return crud.get_all_wheel_specifications(db)
