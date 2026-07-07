"""
Credit Card Fraud Detection - Training Script
"""
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def main():
    df = pd.read_csv('data/creditcard_sampled.csv')
    X = df.drop(['TransactionID', 'Class'], axis=1)
    y = df['Class']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    print("Training Logistic Regression...")
    lr = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
    lr.fit(X_train, y_train)
    print(classification_report(y_test, lr.predict(X_test)))

    print("Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    rf.fit(X_train, y_train)
    print(classification_report(y_test, rf.predict(X_test)))

    with open('models/fraud_model.pkl', 'wb') as f:
        pickle.dump(rf, f)
    with open('models/fraud_scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print("Model saved to models/")

if __name__ == '__main__':
    main()
