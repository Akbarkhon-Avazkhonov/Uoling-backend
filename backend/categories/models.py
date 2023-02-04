from sqlalchemy import Column,Integer, String

from database import Base


class Categories(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    link = Column(String, index=True)
  


