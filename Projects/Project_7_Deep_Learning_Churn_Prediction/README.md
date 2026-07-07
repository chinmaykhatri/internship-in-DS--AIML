# 📉 Project 7: Customer Churn Prediction Engine

<p align="left">
  <img src="https://img.shields.io/badge/Domain-Telecom%20%2F%20CRM-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ML-Random%20Forest%20%2F%20MLP-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Accuracy-84%25%2B-success?style=for-the-badge" />
</p>

## 📋 Executive Overview
Customer churn is one of the highest cost factors for subscription-based enterprises. The **Customer Churn Prediction Engine** analyzes customer demographics, account tenure, billing structures, and service engagement patterns to identify at-risk subscribers. The project implements a comprehensive comparison between traditional machine learning models (Logistic Regression, Decision Trees, Random Forests) and Deep Learning Neural Networks (MLPClassifier).

---

## 🗂️ Directory Architecture
```
Project_7_Deep_Learning_Churn_Prediction/
├── data/
│   └── customer_churn.csv     # 2,000+ subscriber records with 10 features
├── notebooks/
│   ├── EDA_Analysis.ipynb     # In-depth statistical analysis & churn distributions
│   └── Model_Training.ipynb   # Training pipeline & benchmark evaluations
├── src/
│   ├── train.py               # Standalone automated model training script
│   └── predict.py             # Inference script for real-time customer scoring
├── models/
│   ├── best_model.pkl         # Saved high-precision classification model
│   └── scaler.pkl             # Fitted StandardScaler for feature normalization
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## 📊 Exploratory Data Analysis & Findings
* **Tenure Impact**: Customers with a tenure of fewer than 12 months churn at nearly **4x** the rate of long-term subscribers (>36 months).
* **Contract Structure**: Month-to-month contracts exhibit an 80%+ correlation with voluntary churn, whereas 2-year contracts show greater than 95% retention.
* **Financial Drivers**: Higher monthly charges paired with electronic check payments represent the highest-risk segment.

### Model Benchmarks
| Model Architecture | Accuracy | Precision (Churn) | Recall (Churn) | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 84.1% | 0.81 | 0.78 | 0.79 |
| Decision Tree Classifier | 79.5% | 0.74 | 0.72 | 0.73 |
| **Random Forest (Ensemble)** | **86.2%** | **0.85** | **0.82** | **0.83** |
| Multi-Layer Perceptron (NN) | 83.8% | 0.80 | 0.79 | 0.79 |

---

## 💻 How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Models from Scratch
```bash
python src/train.py
```
This script preprocesses `data/customer_churn.csv`, trains all 4 classifiers, displays comparative accuracy metrics, and saves the top-performing model into `models/`.

### 3. Make Live Predictions
```bash
python src/predict.py
```
Encodes sample customer profiles and outputs real-time churn probability predictions.
