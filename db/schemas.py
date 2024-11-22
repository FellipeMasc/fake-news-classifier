from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    is_active: bool = False
    
class UserAuth(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    access_token: str  

class ApiKeyBase(BaseModel):
    key: str
    name: str
    userId: int

class ApiKey(ApiKeyBase):
    id: int
    hashed_key: str
    
class QueryBase(BaseModel):
    query: str

class Query(QueryBase):
    id: int
    response: str
    model: str
    createdAt: datetime
    
class User(UserBase):
    id: int
    queries: List[Query] = []
    api_keys: List[ApiKeyBase] = []
    class Config:
        from_attributes = True

        
class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
    class Config:
        from_attributes = True


    