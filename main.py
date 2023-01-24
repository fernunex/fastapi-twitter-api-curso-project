# Python
from uuid import UUID
from datetime import date
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI, status

# Models
from models import UserBase, UserLogin, User, Tweet

# Path operations 

app = FastAPI()


## AUTHENTICATION

### Register a user
@app.post(
    path="/auth/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=['Authentication']
)
def auth_signup():
    pass

### Login a user
@app.post(
    path="/auth/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=['Authentication']
)
def auth_login():
    pass

## USERS

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=['Users']
)
def show_all_users():
    pass

### Show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=['Users']
)
def show_a_user():
    pass

### Delete a user
@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=['Users']
)
def delete_a_user():
    pass

### Update a user
@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=['Users']
)
def update_a_user():
    pass


## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=['Tweets']
    )
def home():
    return {"Twitter API": "Working!"}

### Post a tweet
@app.post(
    path="/tweets",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=['Tweets']
    )
def post_a_tweet():
    pass

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=['Tweets']
    )
def show_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=['Tweets']
    )
def update_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=['Tweets']
    )
def delete_a_tweet():
    pass