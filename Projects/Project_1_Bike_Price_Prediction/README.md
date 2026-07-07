# 🏍️ Project 1: Used Bike Price Prediction Engine

<p align="left">
  <img src="https://img.shields.io/badge/ML-Regression-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Flask-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-ExtraTreesRegressor-blue?style=for-the-badge" />
</p>

## 📋 Executive Overview
The **Used Bike Price Prediction Engine** is a machine learning web application designed to estimate the fair market resale value of pre-owned motorcycles. By analyzing key vehicle parameters such as mileage, age, brand, engine displacement, and previous ownership history, the system provides accurate price forecasts for sellers and buyers.

---

## 🗂️ Directory Architecture
```
Project_1_Bike_Price_Prediction/
├── app.py                     # Flask web server and routing API
├── Used_Bikes.csv             # Raw dataset (32,000+ motorcycle records)
├── bike_price_model.pkl       # Serialized ExtraTreesRegressor model
├── templates/
│   └── index.html             # Responsive HTML user interface
├── static/                    # CSS stylesheets and UI assets
└── README.md                  # Project documentation
```

---

## 🧠 Machine Learning Methodology
1. **Data Preprocessing**: Cleaned raw motorcycle listings, handled missing numerical values, and encoded categorical features (Brand, Ownership type).
2. **Feature Engineering**: Extracted vehicle age from model year and created normalized mileage-per-year ratios.
3. **Model Selection**: Evaluated Linear Regression, Decision Trees, Random Forests, and **Extra Trees Regressor**.
4. **Model Deployment**: The best-performing model (`ExtraTreesRegressor`) was serialized into `bike_price_model.pkl` and integrated with a lightweight Flask web application.

### Model Performance Benchmarks
| Algorithm | R² Score | Mean Absolute Error (MAE) |
|---|---|---|
| Linear Regression | 0.72 | ₹ 8,450 |
| Random Forest Regressor | 0.88 | ₹ 3,210 |
| **Extra Trees Regressor (Selected)** | **0.91** | **₹ 2,680** |

---

## 💻 How to Run Locally

### 1. Install Requirements
```bash
pip install flask pandas numpy scikit-learn
```

### 2. Launch the Flask Server
```bash
python app.py
```

### 3. Access the Web App
Open your browser and navigate to: `http://127.0.0.1:5000`
Input the bike's details (e.g., *Royal Enfield, 350cc, 2018 model, 15,000 kms*) to receive an instant valuation.
