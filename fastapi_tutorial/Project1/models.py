from sqlalchemy import Column , Integer , String
from database import Base


#Table
class User(Base):
    __tablename__ = "Users"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String , index=True)
    email = Column(String , unique=True , index=True)