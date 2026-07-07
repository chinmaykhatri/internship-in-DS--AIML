# Customer Churn Prediction

## Overview
End-to-end data science project predicting customer churn using multiple ML models and a Neural Network.

## Project Structure
```
Project_7_Deep_Learning_Churn_Prediction/
|-- data/
|   |-- customer_churn.csv
|-- notebooks/
|   |-- EDA_Analysis.ipynb
|   |-- Model_Training.ipynb
|-- models/
|   |-- best_model.pkl
|   |-- scaler.pkl
|-- src/
|   |-- train.py
|   |-- predict.py
|-- requirements.txt
|-- README.md
```

## Tools & Libraries
- **Python**, **Pandas**, **NumPy** - Data manipulation
- **Matplotlib**, **Seaborn** - Data visualization
- **Scikit-Learn** - Machine Learning & Neural Networks

## Models Trained
1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. Neural Network (MLPClassifier)

## How to Run
```bash
pip install -r requirements.txt
python src/train.py
python src/predict.py
```
