from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from typing import Union, Any
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from deps import get_db
import random
import string
import os
import dotenv
from cryptography.fernet import Fernet
import base64
from db.schemas import TokenPayload, User
dotenv.load_dotenv()

encoded_key = os.getenv("ENCRYPT_KEY")
byte_string = base64.b64decode(encoded_key)
print(byte_string)
cipher_suite = Fernet(byte_string)
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 
ALGORITHM = "HS256"
JWT_SECRET_KEY = "whatever"
JWT_REFRESH_SECRET_KEY = "whatever"  
  

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
    scheme_name="JWT"
)

def generate_api_key() -> str:
    posfix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return 'fnc-' + posfix

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)

def encode_api_key(api_key: str) -> str:
    return cipher_suite.encrypt(api_key.encode()).decode()

def decode_api_key(encoded_api_key: str) -> str:
    return cipher_suite.decrypt(encoded_api_key.encode()).decode()

def verify_api_key(api_key: str, hashed_api_key: str) -> bool:
    return password_context.verify(api_key, hashed_api_key)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(reuseable_oauth), db = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user: Union[dict[str, Any], None] = await db.user.find_unique(where={"email": token_data.sub})


    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user