# 🛡️ Project 9: Credit Card Fraud Detection Engine

<p align="left">
  <img src="https://img.shields.io/badge/Domain-Cybersecurity%20%2F%20FinTech-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ML-Imbalanced%20Learning%20%2F%20Ensembles-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Accuracy-99.0%25%2B-success?style=for-the-badge" />
</p>

## 📋 Executive Overview
Financial transaction networks face billions of legitimate credit card swipes daily alongside a tiny fraction of fraudulent attempts. The **Credit Card Fraud Detection Engine** addresses the extreme class imbalance challenge (~99.8% legitimate vs. ~0.2% fraudulent) using advanced feature normalization, ensemble decision trees, and classification algorithms optimized for precision and recall.

---

## 🗂️ Directory Architecture
```
Project_9_Credit_Card_Fraud_Detection/
├── data/
│   └── creditcard_sampled.csv # Transaction dataset with PCA-anonymized features (V1-V28)
├── notebooks/
│   ├── Fraud_EDA.ipynb        # Class imbalance visualization & transaction distributions
│   └── Fraud_Model_Training.ipynb # Precision-Recall curves, ROC-AUC, and feature importance
├── src/
│   ├── train.py               # Automated model training and evaluation script
│   └── predict.py             # Live transaction risk scoring inference script
├── models/
│   ├── fraud_model.pkl        # Serialized Random Forest fraud classifier
│   └── fraud_scaler.pkl       # Fitted StandardScaler for transaction amounts
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## 🧠 Tackling Extreme Class Imbalance
In fraud detection, standard overall accuracy is misleading (predicting "No Fraud" every time yields 99.8% accuracy but catches zero criminals). This project prioritizes:
1. **Stratified Sampling**: Ensuring exact class ratios are preserved across training and validation splits.
2. **Feature Scaling**: Standardizing transaction monetary values (`Amount`) using `StandardScaler` to prevent high-value transactions from skewing decision boundaries.
3. **Evaluation Metrics**: Focusing strictly on **Precision** (minimizing false customer freeze alerts), **Recall** (catching real fraud attempts), and the **Precision-Recall Area Under Curve (PR-AUC)**.

### Model Performance Benchmarks
| Algorithm | Overall Accuracy | Fraud Precision | Fraud Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression (Baseline) | 98.5% | 0.75 | 0.96 | 0.84 |
| **Random Forest Classifier** | **99.9%** | **0.95** | **0.80** | **0.87** |

---

## 💻 How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Fraud Classifier
```bash
python src/train.py
```
Ingests transaction records, trains Logistic Regression and Random Forest classifiers, generates detailed classification reports, and exports serialized models to `models/`.

### 3. Score Transactions Real-Time
```bash
python src/predict.py
```
Simulates real-time transaction monitoring, printing instantaneous fraud probability percentages and risk flags.
