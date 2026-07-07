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
    # Load original training data to get all possible dummy columns
    df_train = pd.read_csv('data/customer_churn.csv').drop(['CustomerID', 'Churn'], axis=1)
    # Combine with new data so get_dummies produces all columns
    combined = pd.concat([df_train, data], ignore_index=True)
    combined_encoded = pd.get_dummies(combined, drop_first=True)
    # Take only the last row(s) which are the new data
    new_encoded = combined_encoded.iloc[-len(data):]
    data_scaled = scaler.transform(new_encoded)
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
    result = predict_churn(sample, model, scaler)[0]
    print(f'Prediction: {"Churn" if result else "No Churn"}')
