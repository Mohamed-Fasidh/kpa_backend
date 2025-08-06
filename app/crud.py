from sqlalchemy.orm import Session
from app import models, schemas

def create_wheel_specification(db: Session, spec: schemas.WheelSpecificationCreate):
    new_spec = models.WheelSpecification(**spec.dict())
    db.add(new_spec)
    db.commit()
    db.refresh(new_spec)
    return new_spec

def get_all_wheel_specifications(db: Session):
    return db.query(models.WheelSpecification).all()
    