from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from database import SessionLocal, engine
from models import DataTable

import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_data(request: Request, db: Session = Depends(get_db)):
    data = db.query(DataTable).all()
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
