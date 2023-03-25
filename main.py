# Python
import json

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
    """
    This path operation shows all tweets in the app

    Parameters:
        -
    
    Returns a json list with all tweets in the app, with the following keys:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read()) # list of dicts
        return results # Fast api can convert this to a json