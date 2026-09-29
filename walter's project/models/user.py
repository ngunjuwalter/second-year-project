from sqlalchemy import Column, String, Float
from db.base import Base

class User(Base):
    """
    Represents a KRA officer profile stored in the database.
    """

    __tablename__ = "users"

    national_id  = Column(String(20), primary_key=True)
    name         = Column(String(50))
    basic_salary = Column(Float)
    extra_income = Column(Float)
    total_income = Column(Float)
