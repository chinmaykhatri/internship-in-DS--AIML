"""
Credit Card Fraud Detection - Prediction Script
"""
import pandas as pd
import numpy as np
import pickle

def predict_transaction(amount, v1, v2, v3, v4, v5):
    with open('models/fraud_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('models/fraud_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    data = np.array([[amount, v1, v2, v3, v4, v5]])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]
    probability = model.predict_proba(data_scaled)[0][1]

    return prediction, probability

if __name__ == '__main__':
    pred, prob = predict_transaction(500, -2, 1.5, -1, 2, -1.5)
    status = "FRAUD" if pred else "NORMAL"
    print(f"Prediction: {status} (Fraud Probability: {prob:.2%})")
