from typing import List
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response
from deps import get_db
from auth.main import encode_api_key, generate_api_key, get_current_user, decode_api_key
from db.schemas import ApiKeyBase, Query, User

predicters_router = APIRouter(
    prefix="/predicters",
    tags=["predicters"]
)

@predicters_router.get('/logistic_regression', summary="Classificar fake news usando regressão logística.", response_model=List[ApiKeyBase])
async def get_user_details(api_key = str,db = Depends(get_db)):
    pass

@predicters_router.get('/decision_tree', summary="Classificar fake news usando regressão logística.", response_model=List[ApiKeyBase])
async def get_user_details(api_key = str,db = Depends(get_db)):
    pass

@predicters_router.get('/random_forest', summary="Classificar fake news usando regressão logística.", response_model=List[ApiKeyBase])
async def get_user_details(api_key = str,db = Depends(get_db)):
    pass

@predicters_router.get('/gradient_boosting', summary="Classificar fake news usando regressão logística.", response_model=List[ApiKeyBase])
async def get_user_details(api_key = str,db = Depends(get_db)):
    pass

                                           