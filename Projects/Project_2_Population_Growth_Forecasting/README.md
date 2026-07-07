# 🌍 Project 2: Population Growth & Demographic Forecasting

<p align="left">
  <img src="https://img.shields.io/badge/Domain-Demographics-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Technique-Polynomial%20Regression-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Analysis-Jupyter%20Notebook-green?style=for-the-badge" />
</p>

## 📋 Executive Overview
Understanding demographic trajectories is vital for urban planning, resource allocation, and economic policymaking. This project leverages historical census and population data to perform deep exploratory data analysis (EDA) and apply polynomial regression and time-series forecasting techniques to predict future population growth rates across various regions.

---

## 🗂️ Directory Architecture
```
Project_2_Population_Growth_Forecasting/
├── population_forecasting.ipynb   # Complete analysis and modeling notebook
├── population_data.csv            # Historical demographic dataset
├── visual_reports/                # Generated demographic charts & trends
└── README.md                      # Project documentation
```

---

## 🔍 Key Analytical Findings
* **Urban vs. Rural Shift**: Analysis reveals a consistent accelerating migration toward urban centers over the last three decades, with urban growth outpacing rural growth by **3.2x**.
* **Non-Linear Growth Trajectory**: Standard linear models fail to capture population saturation and inflection points. A **Degree-3 Polynomial Regression** model successfully maps historical curves with an R² accuracy of **0.965**.
* **Long-Term Projections**: The model projects regional population stabilization timelines, assisting infrastructure planners in optimizing water, electricity, and transit investments.

---

## 💻 How to Run Locally

### 1. Install Requirements
```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 2. Launch Jupyter Notebook
```bash
jupyter notebook population_forecasting.ipynb
```
Run the interactive cells sequentially to generate historical trend visualizations and future forecast curves.
