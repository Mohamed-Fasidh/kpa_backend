from pydantic import BaseModel
from typing import Optional

class WheelSpecificationCreate(BaseModel):
    wheel_number: str
    diameter: float
    thickness: float
    pressure: float
    remarks: Optional[str] = None

class WheelSpecificationOut(WheelSpecificationCreate):
    id: int

    class Config:
        from_attributes = True
