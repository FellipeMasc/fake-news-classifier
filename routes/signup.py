from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from auth.main import create_access_token, get_hashed_password
from db.schemas import UserBase, UserOut, UserAuth
from deps import get_db
from uuid import uuid4
from prisma.models import User
from fastapi import Depends, APIRouter

signup_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@signup_router.post('/signup', summary="Criar um novo usuário.", response_model=UserOut)
async def create_user(data: UserAuth, db=Depends(get_db)):
    user = await db.user.find_unique(
        where={
            "email": data.email
        }
    )
    if user:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password)
    }
    
    user_db = await db.user.create(
        data={
            "email": user['email'],
            "password": user['password']
        }
        )  
    return {
        "id": user_db.id,
        "is_active": user_db.is_active,
        "email": user_db.email,
        "access_token": create_access_token(user["email"])
    }