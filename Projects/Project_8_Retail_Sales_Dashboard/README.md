# 🛒 Project 8: Retail Sales Executive Analytics Dashboard

<p align="left">
  <img src="https://img.shields.io/badge/Domain-Retail%20BI-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Visualization-Plotly%20Interactive-green?style=for-the-badge" />
</p>

## 📋 Executive Overview
In modern retail, real-time data visibility drives profitability. The **Retail Sales Executive Analytics Dashboard** is an interactive web-based Business Intelligence application built with **Streamlit** and **Plotly**. It ingests transactional sales data and transforms it into actionable executive KPIs, geographical performance maps, category revenue breakdowns, and seasonal demand trends.

---

## 🗂️ Directory Architecture
```
Project_8_Retail_Sales_Dashboard/
├── app.py                     # Streamlit dashboard application code
├── data/
│   └── retail_sales.csv       # Transactional retail records (Revenue, Profit, Category, Region)
├── notebooks/
│   └── Sales_EDA.ipynb        # In-depth exploratory data analysis & aggregations
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## 🌟 Dashboard Key Features
* **🎯 Real-Time KPI Cards**: Dynamic calculation of Total Revenue, Total Net Profit, Total Units Sold, and Average Order Value (AOV).
* **🔍 Interactive Sidebar Filters**: Slice and dice metrics instantly by geographical region (*North, South, East, West*) and product category (*Electronics, Clothing, Furniture, Groceries*).
* **📈 Multi-Dimensional Charts**:
  * **Monthly Revenue Trajectory**: Interactive Plotly line charts capturing seasonal demand peaks.
  * **Category Profitability**: Bar charts comparing gross revenue against net margins per department.
  * **Regional Performance Distribution**: Sunburst charts and pie charts highlighting top-performing territories.

---

## 💻 How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch Streamlit Executive Dashboard
```bash
streamlit run app.py
```
Open your web browser at `http://localhost:8501`. Use the interactive sidebar to filter by region or product category and observe instantaneous KPI updates.
