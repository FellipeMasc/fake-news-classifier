import asyncio
from prisma import Prisma
from collections.abc import Generator
from typing import Annotated
from typing import AsyncGenerator
from fastapi import Depends
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

async def simulate_request_response_from_trained_model(model_name: str, input_data: str) -> str:
    await asyncio.sleep(1)
    model = joblib.load(f"./datascience/data/fake_news_{model_name}_model.pkl")
    input_data = [input_data]
    vectorization = joblib.load('./datascience/data/vectorizer.pkl')
    input_data = vectorization.transform(input_data)
    response = model.predict(input_data)
    
    return "True Fact" if response[0] == 1 else "Fake News"


async def get_db() -> AsyncGenerator[Prisma, None]:
    db = Prisma()
    await db.connect()
    try :
        yield db
    finally:
        await db.disconnect()
        
