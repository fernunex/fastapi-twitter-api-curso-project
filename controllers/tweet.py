# Python
from typing import List

# FastAPI
from fastapi import APIRouter, status

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
def post_a_tweet():
    pass

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