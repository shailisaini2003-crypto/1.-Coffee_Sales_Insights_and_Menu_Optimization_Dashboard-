# ☕ Afficionado Coffee Roasters - Product Optimization & Revenue Analysis

An End-to-End Data Science and Business Intelligence Dashboard built using **Python, Streamlit, and Plotly** to analyze transactional data, optimize product menus, and uncover revenue contribution streams.

---

## 🎯 Project Overview
The primary objective of this project is to analyze the sales and transaction data of **Afficionado Coffee Roasters** to solve core business inventory and menu challenges:
- **Revenue Concentration:** Identify which menu items drive the bulk of the business income.
- **Menu Optimization:** Filter out underperforming items (Long-tail stock) to minimize waste and storage inventory costs.
- **Store Performance Matrix:** Provide interactive market analysis across multiple retail locations.

---

## 🛠️ Tech Stack & Architecture
- **Environment:** Google Colab Cloud Back-end
- **Language:** Python 3.x
- **Data Manipulation:** Pandas & NumPy
- **Interactive UI Framework:** Streamlit Framework
- **Dynamic Visualizations:** Plotly Express Grid (Bar, Pie, and Scatter Plots)
- **Version Control & Deployment:** GitHub Workspace & Streamlit Cloud Engine

---

## 📊 Core Dashboard Features
1. **Business KPIs:** Real-time visibility into **Total Revenue**, **Sales Volume (Units)**, and **Unique Products SKU counts**.
2. **Top Performing Products Analytics:** Interactive horizontal bar charts showcasing the highest-revenue generators with a dynamic **Top-N Slider** filter.
3. **Category Revenue Share:** Donut/Pie charts mapping out corporate dependency on product divisions (Coffee vs Tea vs Drinking Chocolate vs Bakery).
4. **Product Strategy Matrix (Scatter Analysis):** A 2D diagnostic visual mapping Sales Volume (Popularity) against Total Revenue to instantly separate **"Hero Products"** from low-performing inventory.

---

## 📥 File Directory Structure
Ensure your root workspace is arranged exactly as shown below:
```text
coffee-sales-dashboard/
│
├── dataset.csv          # Standardized Cleaned Transactional Dataset
├── app.py               # Core Streamlit Web Application Code Script
├── requirements.txt     # Virtual Environment Dependency Setup Configurations
└── README.md            # Professional Portfolio Documentation File
```

---

## 🚀 Execution & Deployment Manual
To run this project locally, execute the following commands in your command terminal:

1. **Install Dependencies:**
   ```bash
   pip install streamlit pandas plotly openpyxl
   ```

2. **Launch Streamlit Web Engine:**
   ```bash
   streamlit run app.py
   ```
