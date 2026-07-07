# 📈 Project 4: Deep Learning Stock Price Prediction Engine

<p align="left">
  <img src="https://img.shields.io/badge/Deep%20Learning-LSTM%20%2F%20RNN-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Domain-FinTech-blue?style=for-the-badge" />
</p>

## 📋 Executive Overview
Financial markets are notoriously volatile and complex. This project builds a **Long Short-Term Memory (LSTM)** neural network capable of capturing long-term temporal dependencies in historical stock market data to forecast closing prices. Integrated with an interactive **Streamlit dashboard**, users can visualize moving averages, trend indicators, and future price trajectories in real time.

---

## 🗂️ Directory Architecture
```
Project_4_Stock_Price_Prediction/
├── app.py                     # Streamlit interactive web dashboard
├── stock_model_lstm.h5        # Trained Keras LSTM deep learning model
├── data/
│   └── historical_stock_data.csv # Multi-year daily stock price records
├── notebooks/
│   └── LSTM_Training.ipynb    # Deep learning architecture exploration
└── README.md                  # Project documentation
```

---

## 🧠 Deep Learning Architecture (LSTM)
* **Sequence Windowing**: Data is formatted into 60-day sliding time windows ($X_{t-60} \dots X_{t-1}$) to predict day $X_t$.
* **Network Layers**:
  * Layer 1: LSTM (50 units, return sequences = True) + Dropout (0.2)
  * Layer 2: LSTM (50 units, return sequences = False) + Dropout (0.2)
  * Layer 3: Dense Output Layer (1 unit, Linear activation for continuous price estimation)
* **Optimization**: Trained using the **Adam optimizer** and **Mean Squared Error (MSE)** loss function over 50 epochs.

---

## 💻 How to Run Locally

### 1. Install Requirements
```bash
pip install streamlit tensorflow keras pandas numpy matplotlib scikit-learn yfinance
```

### 2. Launch Streamlit Dashboard
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`, input any stock ticker symbol (e.g., `AAPL`, `GOOGL`, `TCS.NS`), and explore interactive price predictions.
