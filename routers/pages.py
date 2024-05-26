import json
from fastapi import HTTPException, routing, APIRouter
from fastapi import Depends
from fastapi.responses import HTMLResponse,Response
from sqlalchemy.orm import Session
from model import StaticPages, Profile
from pydantic import BaseModel, Field
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
routers = APIRouter()

# Database setup
DATABASE_URL = "sqlite:///./profile123.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class StaticPagesRequest(BaseModel):
    Heading : str
    Content : str

class ProfileRequest(BaseModel):
    Id : str
    Name : str
    DOB : str
    Address : str
    Zip : str
    Email : str
    Phone : str
    Resume : str

# @routers.get("/")
# async def get_static_pages():
#     return {
#         "Home": "Home content",
#         "Aboutus": "About us content"
#         } 

@routers.get("/allpages", status_code=200)
async def get_allpages(db: Session = Depends(get_db)):
    
    pages_model = db.query(StaticPages).all()
    if pages_model is None:
        raise HTTPException(400, detail="Record not found")
    
    Response.headers = "application/json"
    #html_content =json.loads(pages_model)
    return Response(content= json.loads(pages_model), media_type="application/json")

@routers.get("/profile", status_code=200)
async def get_profile(db: Session = Depends(get_db)):
    profile_model = db.query(Profile).all()
    if profile_model is None:
        raise HTTPException(400, detail="Record not found")
    
    return profile_model