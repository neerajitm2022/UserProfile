from fastapi import routing, APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from model import Profile
from pydantic import BaseModel, Field
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
routers = APIRouter()

# # Database setup
# DATABASE_URL = "sqlite:///./profile.db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



