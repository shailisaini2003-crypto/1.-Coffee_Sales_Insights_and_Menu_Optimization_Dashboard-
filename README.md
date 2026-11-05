# ☕ Afficionado Coffee Roasters - Product Optimization & Revenue Analysis

An End-to-End Data Science and Business Intelligence Dashboard built using **Python, Streamlit, and Plotly** to analyze transactional store data, optimize product menus, and uncover net revenue contribution streams.

---

## 🎯 Project Overview
The primary objective of this project is to analyze the sales and transaction logs of **Afficionado Coffee Roasters** to solve core business inventory challenges:
- **Revenue Concentration:** Identify which high-margin menu items drive the bulk of business profits.
- **Menu Optimization:** Filter out underperforming items (low-velocity stock) to minimize storage and wastage costs.
- **Location Performance Matrix:** Provide interactive market analysis across multiple metropolitan retail locations.

---

## 🛠️ Tech Stack & Architecture
- **Environment:** Google Colab Cloud Development Workspace
- **Language:** Python 3.x
- **Data Manipulation:** Pandas & NumPy Processing
- **Interactive UI Framework:** Streamlit Framework
- **Dynamic Visualizations:** Plotly Express Engine (Horizontal Bar, Hole Pie, and 2D Scatter Matrix Plots)
- **Version Control & Hosting:** GitHub Repository Workspace & Streamlit Cloud Engine

---

## 📊 Core Dashboard Features
1. **Business Metrics KPIs:** Real-time visibility into **Total Revenue (\$)**, **Sales Volume (Units)**, and **Unique Products SKU Count**.
2. **Top Performing Products Analytics:** Interactive horizontal bar charts showcasing the highest-revenue generators with an integrated dynamic **Top-N Slider** layout.
3. **Category Revenue Share:** Specialized donut/pie charts mapping corporate reliance on product divisions (Coffee vs Tea vs Drinking Chocolate vs Bakery).
4. **Product Strategy Matrix (Scatter Analysis):** A 2D diagnostic matrix mapping Sales Volume (Popularity) against Total Generated Revenue to instantly separate **"Hero Products"** from bottleneck stock.

---

## 📥 File Directory Structure
Ensure your GitHub root repository contains exactly the following file names:
```text
coffee-sales-dashboard/
│
├── dataset.xlsx         # Standardized Cleaned Excel Transactional Dataset
├── app.py               # Core Streamlit Web Application Production Script
├── requirements.txt     # Virtual Environment Dependency Setup Configurations
└── README.md            # Professional Portfolio Documentation File
```

---

## 🚀 Local Execution Manual
To run this interactive interface dashboard project locally on your machine, execute the following commands in your command terminal:

1. **Install Project Dependencies:**
   ```bash
   pip install streamlit pandas plotly openpyxl
   ```

2. **Launch Streamlit Web Engine Runtime:**
   ```bash
   streamlit run app.py
   ```
