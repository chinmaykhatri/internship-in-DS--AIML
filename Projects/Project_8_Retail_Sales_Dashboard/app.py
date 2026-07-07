import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛍️ Retail Sales Interactive Dashboard")
st.markdown("Analyze daily sales performance across different product categories.")

@st.cache_data
def load_data():
    df = pd.read_csv('retail_sales.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

category = st.selectbox("Select Category to Analyze:", ['Electronics', 'Clothing', 'Groceries'])

fig = px.line(df, x='Date', y=category, title=f"{category} Sales Trend (2023)")
st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label=f"Total {category} Sales", value=f"${np.sum(df[category]):,.2f}")
with col2:
    st.metric(label=f"Average Daily Sales", value=f"${np.mean(df[category]):,.2f}")
with col3:
    st.metric(label="Max Single Day Sale", value=f"${np.max(df[category]):,.2f}")
