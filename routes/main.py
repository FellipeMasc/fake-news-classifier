from fastapi import APIRouter
from routes.login import login_router
from routes.signup import signup_router
from routes.users import user_router
from routes.predicters import predicters_router

api_router = APIRouter()

api_router.include_router(signup_router)
api_router.include_router(login_router)
api_router.include_router(user_router)
api_router.include_router(predicters_router)
