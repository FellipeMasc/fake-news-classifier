from fastapi import FastAPI
from routes.main import api_router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.include_router(api_router)

