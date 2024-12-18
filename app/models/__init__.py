from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Calculation(Base):
    __tablename__ = "calculations"
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, nullable=False)
    result = Column(String, nullable=False)
