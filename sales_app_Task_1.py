import streamlit as st
import pandas as pd

# Title and subheader
st.title("Sales Summary Dashboard")
st.subheader("An interactive app to explore sales data by category")

# Create hardcoded DataFrame with 5 rows and 3 columns
data = {
    'Product': ['Laptop', 'Mouse', 'Chair', 'Desk', 'Monitor'],
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics'],
    'Sales': [1200, 25, 350, 480, 650]
}

df = pd.DataFrame(data)

# Add selectbox for filtering by Category
category_filter = st.selectbox(
    "Select a Category:",
    options=df['Category'].unique()
)

# Filter the DataFrame based on selected category
filtered_df = df[df['Category'] == category_filter]

# Display filtered DataFrame
st.dataframe(filtered_df)