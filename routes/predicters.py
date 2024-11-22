from typing import List
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response
from deps import get_db, simulate_request_response_from_trained_model
from auth.main import encode_api_key, generate_api_key, get_current_user, decode_api_key
from db.schemas import ApiKeyBase, Query, User

predicters_router = APIRouter(
    prefix="/predicters",
    tags=["predicters"]
)

@predicters_router.get('/logistic_regression', summary="Classificar fake news usando regressão logística.", response_model=str)
async def get_user_details(api_key = str, input = str, db = Depends(get_db)):
    
    #verify api key
    api_key_db = await db.apikey.find_first(where={"key": api_key})
    if not api_key_db:
        raise HTTPException(status_code=400, detail="Chave de api inválida.")
    #verify user
    user = await db.user.find_first(where={"id": api_key_db.userId})
    response = await simulate_request_response_from_trained_model("lr", input)
    
    query = await db.query.create(data={"query": input, "response": response, "model": "regressão logística", "userId": user.id})
    
    return response

@predicters_router.get('/decision_tree', summary="Classificar fake news usando regressão logística.", response_model=List[ApiKeyBase])
async def get_user_details(api_key = str,db = Depends(get_db)):
    pass

@predicters_router.get('/random_forest', summary="Classificar fake news usando regressão logística.", response_model=List[ApiKeyBase])
async def get_user_details(api_key = str,db = Depends(get_db)):
    pass

@predicters_router.get('/gradient_boosting', summary="Classificar fake news usando regressão logística.", response_model=List[ApiKeyBase])
async def get_user_details(api_key = str,db = Depends(get_db)):
    pass

                                           