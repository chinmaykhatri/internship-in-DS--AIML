# Credit Card Fraud Detection

## Overview
Detecting fraudulent transactions in highly imbalanced datasets using Machine Learning with proper evaluation metrics.

## Project Structure
```
Project_9_Credit_Card_Fraud_Detection/
|-- data/
|   |-- creditcard_sampled.csv
|-- notebooks/
|   |-- Fraud_EDA.ipynb
|   |-- Fraud_Model_Training.ipynb
|-- models/
|   |-- fraud_model.pkl
|   |-- fraud_scaler.pkl
|-- src/
|   |-- train.py
|   |-- predict.py
|-- requirements.txt
|-- README.md
```

## Tools & Libraries
- **Python**, **Pandas**, **NumPy** - Data manipulation
- **Matplotlib**, **Seaborn** - Data visualization
- **Scikit-Learn** - Machine Learning (Logistic Regression, Random Forest)

## Key Concepts
- Handling class imbalance with `class_weight='balanced'`
- Precision-Recall curves over Accuracy for imbalanced data
- ROC-AUC analysis
- Feature importance analysis

## How to Run
```bash
pip install -r requirements.txt
python src/train.py
python src/predict.py
```
