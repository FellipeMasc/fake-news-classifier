from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from db.schemas import TokenSchema
from deps import get_db
from auth.main import (
    get_hashed_password,
    create_access_token,
    verify_password
)
from uuid import uuid4

login_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@login_router.post('/login', summary="Criar a sessão e retornar o token de acesso.", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = await db.user.find_unique(where={"email": form_data.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = get_hashed_password(form_data.password)
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.email),
        "token_type": "bearer"
    }