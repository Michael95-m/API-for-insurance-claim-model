from typing import Any

import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from insurance_claim_model import __version__ as model_version
from insurance_claim_model.predict import predict_data
from loguru import logger

from app import schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/info", response_model=schemas.Info, status_code=200)
def info() -> dict:
    info_data = {
        "name": "Insurance Claim Prediction",
        "api_version": settings.API_V1_STR,
        "model_version": model_version,
    }

    return info_data


@api_router.post("/predict", response_model=schemas.PredictResults, status_code=200)
async def predict(input_data: schemas.MultipleInsuranceInputs) -> Any:

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"Make prediction at: {input_df}")
    results = predict_data(input_data=input_df)

    if results["errors"] is not None:
        logger.info(f"Prediction error: {results.get('errors')}")
        raise HTTPException(
            status_code=400, detail=f"Prediction error {results('errors')}"
        )

    logger.info(f"Prediction results: {results['predictions']}")

    return results
