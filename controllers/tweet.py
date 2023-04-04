# Python
from typing import List, Optional
from uuid import UUID
import json
from datetime import datetime

# FastAPI
from fastapi import APIRouter, status, Body, Path, HTTPException, Form

# Models
from models import Tweet


router = APIRouter(
    prefix='/tweets',
    tags=['Tweets']
)


# Tweets

# Show all tweets
@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets"
    )
def get_all_tweets():
        """
    Show all Tweets

    This path operation show all tweets in the app

    Parameters:
        - any

    Return a json list with all tweets in the app, with the following keys:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
        with open('tweets.json', 'r', encoding='utf-8') as f:
            results = json.loads(f.read())
            return results

# Post a tweet


@router.post(
    path="/",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet"
    )
def post_a_tweet(tweet: Tweet = Body(...)):
    """
    Post a Tweet

    This path operation posts a tweet in the app

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
        tweet = tweet.dict()
        tweet["tweet_id"] = str(tweet["tweet_id"])
        tweet["created_at"] = str(tweet["created_at"])

        if tweet["updated_at"]:
            tweet["updated_at"] = str(tweet["updated_at"])

        tweet['by']['user_id'] = str(tweet['by']['user_id'])
        tweet['by']['birth_date'] = str(tweet['by']['birth_date'])

        results.append(tweet)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

# Show a tweet

# Check the video of raising errors https://platzi.com/clases/2514-fastapi-errores/41987-httpexception/
@router.get(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet"
    )
def show_a_tweet(
    tweet_id: UUID = Path(...)
    ):
        """
    Show a tweet

    This path operation shows a specific tweet in the app

    Parameters:
        - Path parameter
            - tweet_id: UUID

    Return a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
        with open('tweets.json', 'r', encoding='utf-8') as f:
            results = json.loads(f.read())
            for tweet in results:
                if tweet['tweet_id'] == str(tweet_id):
                    return tweet
            
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tweet not found!"
            )

### Update a tweet
@router.put(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet"
    )
def update_a_tweet(
    tweet_id: UUID = Path(...),
    content_update: str = Form(
        ...,
        min_length=2,
        max_length=256)
    ):
    """
    Update a tweet

    This path operation updates a specific tweet in the app

    Parameters:
        - Path parameter
            - tweet_id: UUID
            - content_update: str

    Return a json with the basic tweet information updated:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open('tweets.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())

        for tweet in results:
            if tweet['tweet_id'] == str(tweet_id):
                
                # Update the new tweet 
                tweet['content'] = content_update

                tweet["updated_at"] = str(datetime.now())


                with open('tweets.json', 'w', encoding='utf-8') as f:
                    f.seek(0)
                    f.write(json.dumps(results))

                return tweet
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found!"
        )

### Delete a tweet
@router.delete(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet"
    )
def delete_a_tweet(
        tweet_id: UUID = Path(...)
):
    """
    Delete a tweet

    This path operation deletes a specific tweet in the app

    Parameters:
        - Path parameter
            - tweet_id: UUID

    Return a json with the basic tweet deleted information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", 'r', encoding='utf-8') as f:
        results = json.loads(f.read())

        for tweet in results:
            if tweet['tweet_id'] == str(tweet_id):
                results.remove(tweet)

                with open("tweets.json", 'w', encoding='utf-8') as f:
                    f.seek(0)
                    f.write(json.dumps(results))

                return tweet
            
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found!"
        )
