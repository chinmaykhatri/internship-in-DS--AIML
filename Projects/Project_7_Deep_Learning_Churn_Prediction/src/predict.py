"""
Customer Churn Prediction - Prediction Script
Loads saved model and makes predictions on new data.
"""
import pandas as pd
import numpy as np
import pickle

def load_model():
    with open('models/best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('models/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

def predict_churn(data, model, scaler):
    data_encoded = pd.get_dummies(data, drop_first=True)
    data_scaled = scaler.transform(data_encoded)
    predictions = model.predict(data_scaled)
    return predictions

if __name__ == '__main__':
    model, scaler = load_model()
    sample = pd.DataFrame({
        'Gender': ['Male'],
        'Age': [35],
        'Tenure_Months': [12],
        'Monthly_Charges': [80.0],
        'Total_Charges': [960.0],
        'Contract_Type': ['Month-to-month'],
        'Internet_Service': ['Fiber optic'],
        'Payment_Method': ['Electronic Check'],
    })
    print(f'Prediction: {"Churn" if predict_churn(sample, model, scaler)[0] else "No Churn"}')
