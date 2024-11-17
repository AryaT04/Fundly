import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Generate synthetic data
categories = ['Food', 'Rent', 'Utilities', 'Entertainment', 'Transportation', 'Healthcare', 'Shopping']
np.random.seed(42)
n_records = 500
data = {
    'Date': pd.date_range(start='2024-01-01', end='2024-11-30', periods=n_records),
    'Category': np.random.choice(categories, size=n_records),
    'Amount': np.random.uniform(10, 500, size=n_records)
}
spending_data = pd.DataFrame(data)
spending_data['Month'] = spending_data['Date'].dt.to_period('M').astype(str)

# Title and description
st.title("Transaction Patterns Dashboard")
st.markdown("""
This dashboard provides an overview of your spending habits. 
Explore spending trends and identify high-frequency expenses to better manage your finances.
""")

# Filters
st.sidebar.header("Filters")
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [spending_data['Date'].min(), spending_data['Date'].max()]
)
categories_filter = st.sidebar.multiselect(
    "Select Categories",
    options=categories,
    default=categories
)
filtered_data = spending_data[
    (spending_data['Date'] >= pd.Timestamp(start_date)) &
    (spending_data['Date'] <= pd.Timestamp(end_date)) &
    (spending_data['Category'].isin(categories_filter))
]

# Visualizations
st.subheader("Monthly Spending Trend")
monthly_spending = filtered_data.groupby('Month')['Amount'].sum().reset_index()
fig_trend = px.line(monthly_spending, x='Month', y='Amount', title='Monthly Spending Trend')
st.plotly_chart(fig_trend)

st.subheader("Spending by Category")
category_spending = filtered_data.groupby('Category')['Amount'].sum().reset_index()

# Round the Amount column to 2 decimal places
category_spending['Amount'] = category_spending['Amount'].round(2)

fig_category = px.pie(
    category_spending,
    names='Category',
    values='Amount',
    title='Spending by Category',
    color='Category',
    hole=0.3  # Optional: hole=0.3 creates a donut chart instead of a full pie chart
)

# Customize hovertemplate to show values rounded to 2 decimal places
fig_category.update_traces(hovertemplate='%{label}: %{value:.2f}<extra></extra>')

st.plotly_chart(fig_category)


st.subheader("High-Frequency Expenses")
frequency = filtered_data['Category'].value_counts().reset_index()
frequency.columns = ['Category', 'Frequency']
fig_frequency = px.bar(frequency, x='Category', y='Frequency', title='High-Frequency Expenses', color='Category')
st.plotly_chart(fig_frequency)

st.subheader("Spending by Day of the Week")
filtered_data['Day'] = filtered_data['Date'].dt.day_name()

# Ensure days of the week are ordered Sunday to Saturday
day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
filtered_data['Day'] = pd.Categorical(filtered_data['Day'], categories=day_order, ordered=True)

day_spending = filtered_data.groupby('Day')['Amount'].sum().reset_index()
day_spending = day_spending.sort_values(by='Day')  # Sort by the custom order
fig_day = px.bar(day_spending, x='Day', y='Amount', title='Spending by Day of the Week', color='Day')
st.plotly_chart(fig_day)


st.download_button(
    label="Download Data",
    data=filtered_data.to_csv(index=False),
    file_name='filtered_spending_data.csv',
    mime='text/csv'
)
