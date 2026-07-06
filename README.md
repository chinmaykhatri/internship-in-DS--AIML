# 📊 Data Science & AI/ML — Summer Internship Training Program

> A structured, hands-on training journey through **Python programming**, **Data Analysis**, **Machine Learning**, and **Web-based Dashboard Development**, completed under the **GRRAS Solutions** internship program (SITP).

---

## 🎯 Program Overview

This repository documents a **45-day intensive training** covering the complete Data Science pipeline — from Python fundamentals to building production-ready ML models and interactive analytics dashboards. Each day builds on the previous one, progressing from core programming concepts to advanced machine learning techniques.

---

## 🗂️ Repository Structure

```
├── README.md
└── GRASS/
    ├── Day_1.py  –  Day_19.py      # Python fundamentals & libraries (.py scripts)
    ├── Day_20.ipynb – Day_34.ipynb  # Advanced ML & analysis (Jupyter Notebooks)
    ├── Mini_Project_1.py            # Student Management System (OOP)
    ├── Assessment_1.ipynb           # Comprehensive skills assessment
    ├── app.py                       # Streamlit E-Commerce Analytics Dashboard
    ├── ecommerce_sales.ipynb        # E-Commerce sales analysis project
    ├── Diamond_price_prediction.ipynb  # ML regression model project
    ├── *.csv / *.json / *.xlsx      # Datasets used across exercises
    └── *.png / *.jpg                # Generated plots and visualizations
```

---

## 📅 Day-by-Day Curriculum

### Phase 1 — Python Fundamentals (Days 1–6)

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| **Day 1** | Variables & Memory | Variable declaration, `id()`, memory referencing |
| **Day 2** | Type Conversion & Operators | `input()`, type casting, arithmetic & logical operators |
| **Day 3** | Conditional Statements | `if`, `elif`, `else`, nested conditions |
| **Day 4** | Functions | `def`, parameters, `*args`, `**kwargs`, lambda, recursion |
| **Day 5** | Data Structures — Dictionaries | `.get()`, `.keys()`, `.values()`, `.items()`, nested dicts |
| **Day 6** | Modules & Imports | `math`, `random`, `os`, custom modules |

### Phase 2 — Object-Oriented Programming (Days 7–8)

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| **Day 7** | OOP Fundamentals | Classes, Objects, `__init__`, Encapsulation, Inheritance, Polymorphism |
| **Day 8** | Class Methods & `self` | Instance methods, class attributes, method chaining |

### Phase 3 — NumPy (Days 9–12)

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| **Day 9** | NumPy Introduction | Arrays vs Lists, performance comparison, `ndarray` |
| **Day 10** | Array Operations | Indexing, slicing, broadcasting, mathematical operations |
| **Day 11** | Array Reshaping | `reshape()`, `flatten()`, `ravel()`, `transpose()` |
| **Day 12** | Sorting & Aggregation | `sort()`, axis-based sorting, statistical functions |

### Phase 4 — Pandas (Days 13–18)

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| **Day 13** | Pandas Introduction | Series, DataFrames, reading data |
| **Day 14** | Series & DataFrames | 1D Series, 2D DataFrames, indexing |
| **Day 15** | Data Reading & Exploration | `read_json()`, `head()`, `tail()`, `describe()`, `info()` |
| **Day 16** | Data Manipulation | Filtering, column operations, `apply()`, `groupby()` |
| **Day 17** | Sorting & Aggregation | `sort_values()`, `agg()`, multi-column sorting |
| **Day 18** | Handling Missing Values | `isnull()`, `fillna()`, `dropna()`, imputation strategies |

### Phase 5 — Data Visualization (Day 19)

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| **Day 19** | Matplotlib | Line plots, bar charts, scatter plots, subplots, styling |

### Phase 6 — Machine Learning & Advanced Analysis (Days 20–34)

| Day | Topic | Format |
|-----|-------|--------|
| **Day 20** | Exploratory Data Analysis (EDA) | Jupyter Notebook |
| **Day 21** | Advanced EDA & Feature Engineering | Jupyter Notebook |
| **Day 24** | Supervised Learning Foundations | Jupyter Notebook |
| **Day 25** | Classification Algorithms | Jupyter Notebook |
| **Day 26** | Regression Models | Jupyter Notebook |
| **Day 27** | Model Evaluation & Metrics | Jupyter Notebook |
| **Day 29** | Advanced ML Techniques | Jupyter Notebook |
| **Day 30** | Ensemble Methods | Jupyter Notebook |
| **Day 31** | Deep Learning Introduction | Jupyter Notebook |
| **Day 32** | Neural Network Implementation | Jupyter Notebook |
| **Day 33** | Model Optimization | Jupyter Notebook |
| **Day 34** | Final Review & Best Practices | Jupyter Notebook |

---

## 🚀 Projects

### 1. Student Management System — `Mini_Project_1.py`
An OOP-based console application for managing student records with full CRUD operations — create, read, update, and delete student entries using classes and methods.

### 2. E-Commerce Sales Analysis — `ecommerce_sales.ipynb`
End-to-end exploratory analysis of an e-commerce dataset (`ecommerce_sales_data.csv`) with:
- Sales trend identification
- Customer segmentation
- Revenue pattern analysis
- Data cleaning and visualization

### 3. E-Commerce Analytics Dashboard — `app.py`
A **Streamlit**-powered interactive web dashboard built with Plotly, Seaborn, and Matplotlib for real-time e-commerce data exploration and KPI tracking.

### 4. Diamond Price Prediction — `Diamond_price_prediction.ipynb`
A complete ML regression pipeline using the `diamonds.csv` dataset:
- Feature engineering (carat, cut, color, clarity)
- Model training and evaluation
- Price prediction with a serialized model (`diamond_price_model.pkl`)

---

## 🛠️ Tech Stack

| Category | Tools & Libraries |
|----------|------------------|
| **Language** | Python 3.x |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Machine Learning** | Scikit-learn |
| **Deep Learning** | TensorFlow / Keras |
| **Web Dashboard** | Streamlit |
| **Notebooks** | Jupyter Notebook |
| **Serialization** | Pickle |

---

## 📊 Datasets Included

| File | Description |
|------|-------------|
| `diamonds.csv` | 50,000+ diamond records with carat, cut, color, clarity, and price |
| `ecommerce_sales_data.csv` | E-commerce transaction records for sales analysis |
| `student-data.json` | Student records for Pandas exercises |
| `temperature_data.json` | Temperature readings for data manipulation practice |
| `data.json` | General-purpose JSON dataset |
| `file1.csv`, `file1.json`, `file1.xlsx`, `file2.json` | Multi-format datasets for I/O exercises |

---

## 📈 Sample Visualizations

The repository includes generated plots demonstrating various visualization techniques:
- Line charts and bar graphs
- Subplots and multi-panel figures
- Statistical distribution plots

---

## 📜 License

This project is part of an academic internship program and is intended for educational purposes.

---

## 🙏 Acknowledgements

- **GRRAS Solutions** — For providing the structured training program and mentorship
- **SITP (Summer Internship Training Program)** — For the opportunity to learn and apply Data Science concepts hands-on

---

<p align="center">
  <i>Built with 💡 curiosity and ☕ code during the Data Science & AI/ML internship at GRRAS Solutions</i>
</p>
