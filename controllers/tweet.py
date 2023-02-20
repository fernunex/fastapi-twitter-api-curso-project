# Python
from typing import List
import json

# FastAPI
from fastapi import APIRouter, status, Body

# Models
from models import Tweet


router = APIRouter(
    prefix='/tweets',
    tags=['Tweets']
)


## Tweets

### Show all tweets
@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets"
    )
def get_all_tweets():
    pass

### Post a tweet
@router.post(
    path="/",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet"
    )
def post_a_tweet(tweet: Tweet = Body(...)):
    """
    Post a Tweet

    This path operation post a tweet in the app

    Parameters:
        - Request body parameter
            - tweet : Tweet 
    
    Return a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])

        if tweet_dict["updated_at"]:
            tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])



        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

### Show a tweet
@router.get(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet"
    )
def show_a_tweet():
    pass

### Update a tweet
@router.put(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet"
    )
def update_a_tweet():
    pass

### Delete a tweet
@router.delete(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet"
    )
def delete_a_tweet():
    pass