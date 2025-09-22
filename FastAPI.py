import pandas as pd
from fastapi import FastAPI
from schema.pydanticmodel import StudentValidation
from model.model import scaler, model

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Student Result Predictor API'}

@app.get('/health')
def health():
    return {
        'Status': 'ok',
        'Model is Loaded': model is not None
    }

@app.post('/Result')
def predict(input: StudentValidation):
   
    data = pd.DataFrame([{
        'StudyHours': input.studyhours,
        'Attendance': input.attendance,
        'PastScore': input.pastscore,
        'SleepHours': input.sleephours
    }])

    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)[0]

    result = 'PASS' if prediction == 1 else 'FAIL'
    return result
