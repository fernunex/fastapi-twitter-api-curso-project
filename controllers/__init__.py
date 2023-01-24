# Fast API
from fastapi import APIRouter

# Routers
from .auth import router as auth_router
from .tweet import router as tweet_router
from .user import router as user_router

# General router

router = APIRouter(
    prefix='/api'
)

router.include_router(auth_router)
router.include_router(tweet_router)
router.include_router(user_router)
