import sqlalchemy.orm
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
Base = sqlalchemy.orm.declarative_base()

class StaticPages(Base):
    __tablename__ = "StaticPages"
    Id = Column(primary_key=True)
    Heading = Column(String)
    Content = Column(String)

class Profile(Base):
    __tablename__ = "Profile"
    Id = Column(primary_key=True)
    Name = Column(String)
    DOB = Column(String)
    Address = Column(String)
    Zip = Column(String)
    Email = Column(String)
    Phone = Column(String)
    Resume = Column(String)