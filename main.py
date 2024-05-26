from fastapi import FastAPI, Depends, HTTPException


from pydantic import BaseModel, Field
from model import StaticPages
from routers import pages, profile
app = FastAPI()

app.include_router(pages.routers)
app.include_router(profile.routers)