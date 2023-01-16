# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI

# Models
from models import * #specify

app = FastAPI()



@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}