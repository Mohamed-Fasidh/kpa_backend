from sqlalchemy import Column, Integer, String, Float
from .database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    wheel_number = Column(String, index=True)
    diameter = Column(Float)
    thickness = Column(Float)
    pressure = Column(Float)
    remarks = Column(String, nullable=True)
