from fastapi import APIRouter, HTTPException
import numpy as np

router = APIRouter()

@router.post("/predict")
def predict_movement(data: list):
    try:
        # Assuming ML model is loaded globally for efficiency
        global trained_model
        input_data = np.array(data).reshape((-1, 64, 64, 1))
        predictions = trained_model.predict(input_data)
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
