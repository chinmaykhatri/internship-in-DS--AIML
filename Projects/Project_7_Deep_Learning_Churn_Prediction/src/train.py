"""
Customer Churn Prediction - Training Script
Trains multiple ML models and saves the best one.
"""
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def load_data(path='data/customer_churn.csv'):
    df = pd.read_csv(path)
    df_model = pd.get_dummies(df.drop('CustomerID', axis=1), drop_first=True)
    X = df_model.drop('Churn', axis=1)
    y = df_model['Churn']
    return X, y

def train_models(X_train, y_train, X_test, y_test):
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
        'Neural Network': MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=200, random_state=42),
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
        results[name] = {'model': model, 'accuracy': acc}
        print(f'{name}: Accuracy = {acc:.4f}')
    return results

if __name__ == '__main__':
    X, y = load_data()
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

    results = train_models(X_train, y_train, X_test, y_test)

    best_name = max(results, key=lambda k: results[k]['accuracy'])
    print(f'\nBest Model: {best_name} ({results[best_name]["accuracy"]:.4f})')

    with open('models/best_model.pkl', 'wb') as f:
        pickle.dump(results[best_name]['model'], f)
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print('Saved to models/')
