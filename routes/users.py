from typing import List
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response
from deps import get_db
from auth.main import encode_api_key, generate_api_key, get_current_user
from db.schemas import ApiKeyBase, Query, User

user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@user_router.get('/api_keys', summary="Retornar as chaves de api de um usuário ativo.", response_model=List[ApiKeyBase])
async def get_user_details(user: User = Depends(get_current_user),db = Depends(get_db)):
    api_keys = await db.apikey.find_many(where={"userId": user.id})
    
    response = []
    for api_key in api_keys:
        response.append({
            "key": api_key.key,
            "name": api_key.name,
            "userId": api_key.userId
        })
    return response

@user_router.get('/queries', summary="Enviar para um usuário as suas consultas e o modelo usado.", response_model=List[Query])
async def get_queries_from_document(user: User = Depends(get_current_user), db = Depends(get_db)):
    queries = await db.query.find_many(where={"userId": user.id})

    response = []
    for query in queries:
        response.append({
            "id": query.id,
            "query": query.query,
            "response": query.response,
            "createdAt": query.createdAt,
            "model": query.model
        })
    return response

@user_router.post('/create_api_key', summary="Criar uma nova chave de api para um usuário ativo.", response_model=ApiKeyBase)
async def create_api_key(key_name : str, user: User = Depends(get_current_user), db = Depends(get_db)):
    
    api_key_db = await db.apikey.find_first(where={"name": key_name})
    
    if api_key_db:
        raise HTTPException(status_code=400, detail="A chave de api já existe.")
    api_key_hash = generate_api_key(key_name)
    api_key = await db.apikey.create(data={"key": api_key_hash, "userId": user.id, "name": key_name})
    
    return {
        "key": api_key_hash,
        "name": api_key.name,
        "userId": api_key.userId
    }
                                           