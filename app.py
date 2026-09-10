from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Detector de Fraude em Cartão de Crédito")
templates = Jinja2Templates(directory="templates")

model = joblib.load("fraud_model.pkl")


class TransactionInput(BaseModel):
    distance_from_home: float
    distance_from_last_transaction: float
    ratio_to_median_purchase_price: float
    repeat_retailer: float
    used_chip: float
    used_pin_number: float
    online_order: float

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@app.post("/predict")
def predict_fraud(data: TransactionInput):
    input_df = pd.DataFrame([data.model_dump()])
    
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])

    if probability >= 0.60:
        action = "BLOQUEAR_TRANSACAO"
        status_color = "danger"
        message = "Transação de alto risco detectada. Bloqueio preventivo."
    elif probability >= 0.10:
        action = "SOLICITAR_CONFIRMACAO"
        status_color = "warning"
        message = "Transação atípica. Requer confirmação adicional (biometria)."
    else:
        action = "APROVAR"
        status_color = "success"
        message = "Transação aprovada."

    return {
        "is_fraud": prediction,
        "fraud_probability": round(probability * 100, 2),
        "recommended_action": action,
        "status_color": status_color,
        "message": message
    }