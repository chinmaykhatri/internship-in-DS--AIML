# 🧪 Project 5: Comparative Benchmarking of Regression Architectures

<p align="left">
  <img src="https://img.shields.io/badge/ML-Supervised%20Regression-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Regularization%20%26%20Tuning-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tool-Scikit--Learn-yellow?style=for-the-badge" />
</p>

## 📋 Executive Overview
This rigorous empirical study compares advanced regression techniques on complex, multi-variable datasets. The project explores the mathematical underpinnings of **Ordinary Least Squares (OLS)**, **Ridge ($L_2$ Regularization)**, **Lasso ($L_1$ Regularization)**, **ElasticNet**, and **Polynomial Regression**, highlighting how regularization combats multicollinearity and overfitting in high-dimensional feature spaces.

---

## 🗂️ Directory Architecture
```
Project_5_ML_Project/
├── regression_benchmarks.ipynb # End-to-end mathematical & coding evaluation
├── dataset.csv                 # High-dimensional multi-variable regression data
├── comparative_plots/          # Residual distributions and weight decay graphs
└── README.md                   # Project documentation
```

---

## 📊 Comparative Performance Matrix

| Regression Model | Penalty Type | Best Hyperparameters | Test R² Score | RMSE | Key Takeaway |
|---|---|---|---|---|---|
| **Linear Regression (OLS)** | None | N/A | 0.764 | 4.12 | Prone to variance when collinear features exist. |
| **Ridge Regression** | $L_2$ Norm ($lpha \sum w_i^2$) | $lpha = 10.0$ | 0.821 | 3.45 | Successfully shrinks redundant feature coefficients. |
| **Lasso Regression** | $L_1$ Norm ($lpha \sum \|w_i\|$) | $lpha = 0.1$ | 0.818 | 3.48 | Performs automatic feature selection by zeroing out noisy coefficients. |
| **ElasticNet** | $L_1 + L_2$ Combined | $lpha = 0.5, l_1\_ratio = 0.5$ | **0.835** | **3.21** | Optimal balance between stability and sparsity. |
| **Polynomial Reg (Deg 2)** | None | Degree = 2 | 0.795 | 3.80 | Captures non-linear interactions but increases model complexity. |

---

## 💻 How to Run Locally
```bash
pip install jupyter pandas numpy scikit-learn matplotlib seaborn
jupyter notebook regression_benchmarks.ipynb
```
