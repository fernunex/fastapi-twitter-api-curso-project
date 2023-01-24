# FastAPI
from fastapi import FastAPI

# Controllers
from controllers import router

# Application 

app = FastAPI()

app.include_router(router)

@app.get(
    path='/'
)
def home():
    return {'Hi':'I am working'}