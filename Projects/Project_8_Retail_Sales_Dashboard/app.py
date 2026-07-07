"""
Retail Sales Interactive Dashboard
Built with Streamlit & Plotly
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("Retail Sales Interactive Dashboard")
st.markdown("Analyze daily sales performance across regions, categories, and products.")

@st.cache_data
def load_data():
    df = pd.read_csv('data/retail_sales.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
regions = st.sidebar.multiselect("Region", df['Region'].unique(), default=df['Region'].unique())
categories = st.sidebar.multiselect("Category", df['Category'].unique(), default=df['Category'].unique())

filtered = df[(df['Region'].isin(regions)) & (df['Category'].isin(categories))]

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered['Revenue'].sum():,.0f}")
col2.metric("Total Orders", f"{len(filtered):,}")
col3.metric("Avg Order Value", f"${filtered['Revenue'].mean():,.2f}")
col4.metric("Total Quantity", f"{filtered['Quantity'].sum():,}")

# Revenue Trend
st.subheader("Revenue Trend Over Time")
daily = filtered.groupby('Date')['Revenue'].sum().reset_index()
fig_line = px.line(daily, x='Date', y='Revenue', title='Daily Revenue Trend')
st.plotly_chart(fig_line, use_container_width=True)

# Category & Region Charts
c1, c2 = st.columns(2)
with c1:
    cat_data = filtered.groupby('Category')['Revenue'].sum().reset_index()
    fig_bar = px.bar(cat_data, x='Category', y='Revenue', color='Category', title='Revenue by Category')
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    reg_data = filtered.groupby('Region')['Revenue'].sum().reset_index()
    fig_pie = px.pie(reg_data, values='Revenue', names='Region', title='Revenue by Region')
    st.plotly_chart(fig_pie, use_container_width=True)

# Top Products Table
st.subheader("Top Products by Revenue")
top = filtered.groupby('Product')['Revenue'].sum().sort_values(ascending=False).reset_index()
st.dataframe(top, use_container_width=True)
