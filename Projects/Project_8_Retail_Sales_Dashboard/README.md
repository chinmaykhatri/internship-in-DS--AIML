# Retail Sales Interactive Dashboard

## Overview
A full-stack data analytics project with EDA notebooks and a Streamlit-powered interactive dashboard for retail sales analysis.

## Project Structure
```
Project_8_Retail_Sales_Dashboard/
|-- data/
|   |-- retail_sales.csv
|-- notebooks/
|   |-- Sales_EDA.ipynb
|-- static/
|-- templates/
|-- app.py
|-- requirements.txt
|-- README.md
```

## Tools & Libraries
- **Python**, **Pandas**, **NumPy** - Data manipulation
- **Matplotlib**, **Seaborn** - Static visualization (notebooks)
- **Streamlit**, **Plotly** - Interactive web dashboard

## Features
- Sidebar filters for Region and Category
- KPI metrics (Total Revenue, Orders, Avg Value, Quantity)
- Interactive line, bar, and pie charts
- Top products ranking table

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
