import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page layout and configuration setup
st.set_page_config(page_title="Coffee Roasters Dashboard", layout="wide")

# Data loading and preprocessing function
@st.cache_data
def load_data():
    if os.path.exists("dataset.csv"):
        df = pd.read_csv("dataset.csv")
    elif os.path.exists("dataset.xlsx"):
        df = pd.read_excel("dataset.xlsx")
    else:
        st.error("Error: Dataset file not found in directory.")
        st.stop()
        
    df['transaction_qty'] = pd.to_numeric(df['transaction_qty'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
    df['total_revenue'] = pd.to_numeric(df['total_revenue'], errors='coerce')
    return df.dropna(subset=['transaction_qty', 'unit_price', 'total_revenue'])

try:
    df = load_data()
except Exception as e:
    st.error("Error loading data. Please verify your columns match exactly.")
    st.stop()

# Main Dashboard Header Visuals
st.title("☕ Afficionado Coffee Roasters")
st.subheader("Product Optimization & Revenue Analysis Dashboard")
st.divider()

# Sidebar Filters Navigation Setup
st.sidebar.header("🔧 Dashboard Filters")
locations = ["All Stores"] + list(df['store_location'].unique())
selected_loc = st.sidebar.selectbox("Select Store Location:", locations)

# Filter Data according to user input selection
df_filtered = df if selected_loc == "All Stores" else df[df['store_location'] == selected_loc]
top_n = st.sidebar.slider("Number of Top Products to Display:", min_value=5, max_value=20, value=10)

# Critical Metric KPI Calculations
total_revenue = df_filtered['total_revenue'].sum()
total_units = df_filtered['transaction_qty'].sum()
total_skus = df_filtered['product_detail'].nunique()

# Display core business KPIs in a 3-column Grid Layout
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
kpi2.metric("📦 Total Sales Volume (Units)", f"{int(total_units):,}")
kpi3.metric("🥤 Unique Products (SKU Count)", f"{total_skus}")
st.divider()

# Interactive Graphs & Charts Visualizations Section
col1, col2 = st.columns(2)
with col1:
    st.subheader(f"🔝 Top {top_n} Performing Products (by Revenue)")
    prod_data = df_filtered.groupby('product_detail')['total_revenue'].sum().reset_index().sort_values(by='total_revenue', ascending=False).head(top_n)
    fig1 = px.bar(prod_data, x='total_revenue', y='product_detail', orientation='h', color='total_revenue', color_continuous_scale='YlOrBr')
    fig1.update_layout(yaxis={'categoryorder':'total ascending'}, xaxis_title="Revenue ($)", yaxis_title="Product Name")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("📊 Revenue Contribution Share by Category")
    cat_data = df_filtered.groupby('product_category')['total_revenue'].sum().reset_index()
    fig2 = px.pie(cat_data, values='total_revenue', names='product_category', hole=0.4, color_discrete_sequence=px.colors.sequential.YlOrBr_r)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Scatter Plot Matrix Analysis (Hero vs Low Performing Items Matrix)
st.subheader("🎯 Product Strategy Matrix: Hero vs Underperforming Items")
scatter_data = df_filtered.groupby(['product_detail', 'product_category']).agg(Qty_Sold=('transaction_qty', 'sum'), Revenue=('total_revenue', 'sum')).reset_index()
fig3 = px.scatter(scatter_data, x='Qty_Sold', y='Revenue', text='product_detail', color='product_category', size='Revenue', max_scale_size=30)
fig3.update_layout(xaxis_title="Sales Volume (Popularity)", yaxis_title="Total Generated Revenue ($)")
fig3.update_traces(textposition='top center')
st.plotly_chart(fig3, use_container_width=True)
