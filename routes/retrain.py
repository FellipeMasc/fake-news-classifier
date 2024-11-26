from typing import List
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response
from deps import get_db, simulate_request_response_from_trained_model
from auth.main import encode_api_key, generate_api_key, get_current_user, decode_api_key
from db.schemas import ApiKeyBase, Query, User
from datascience.retrieve import predict_with_model
import pandas as pd
from io import BytesIO
import os

retrain_router = APIRouter(
    prefix="/retrain",
    tags=["retrain"]
)

@retrain_router.get('', summary="Retreinar todos os modelos com algum novo dataset.", response_model=dict)
async def classify_fake_news(instance_name : str,append_in_current : bool, fake_file_csv: bytes = None, true_file_csv: bytes = None, user: User = Depends(get_current_user), db = Depends(get_db)):

    try:
        df_fake = pd.read_csv(BytesIO(fake_file_csv)) if fake_file_csv else None
        df_true = pd.read_csv(BytesIO(true_file_csv)) if true_file_csv else None
        
        if df_fake and 'text' not in df_fake.columns:
            raise HTTPException(status_code=400, detail="Fake CSV must contain a 'text' column")
        if df_true and 'text' not in df_true.columns:
            raise HTTPException(status_code=400, detail="True CSV must contain a 'text' column")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file: {e}")
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_path = os.path.join(root_path, 'datascience', 'data', 'processed.csv')
    if append_in_current:
        existing_df = pd.read_csv(processed_path)
        if df_fake is not None:
            new_df = pd.concat([existing_df, df_fake], ignore_index=True)
            new_df.to_csv(processed_path, index=False)
        
        if df_true is not None:
            new_df = pd.concat([existing_df, df_true], ignore_index=True)
            new_df.to_csv(existing_df, index=False)
    else:
        if df_fake is not None and df_true is not None:
            new_df = pd.concat([df_fake, df_true], ignore_index=True)
            new_df.to_csv(processed_path, index=False)
        elif df_fake is not None:
            df_fake.to_csv(processed_path, index=False)
        elif df_true is not None:
            df_true.to_csv(processed_path, index=False)
    return {"message": "O dado foi salvo com sucesso, espere um tempo para que o novo modelo apareça na interface."}
    
        
        
