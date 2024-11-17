import streamlit as st
import plotly.express as px
import pandas as pd  # Ensure this import is included
from utils.metric import calculate_metrics


def show_dashboard():
    # Title for the dashboard
    st.title("Fundly")

    # Ensure session state is set for balance if not initialized yet
    if 'balance' not in st.session_state:
        st.session_state.balance = 0.0  # Default balance if not set

    # Key Metrics
    metrics = calculate_metrics()
    if not metrics:  # If no transactions available
        st.error("No transactions available for calculations.")
        return

    # Display metrics in columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Current Balance", f"${st.session_state.balance:,.2f}")
    with col2:
        st.metric("Monthly Spending", f"${metrics['total_spending']:,.2f}")
    with col3:
        st.metric("Avg Daily Spending", f"${metrics['avg_daily_spending']:,.2f}")
    with col4:
        st.metric("Monthly Savings", f"${metrics['monthly_savings']:,.2f}")

    # Spending Patterns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Spending by Category")
        # Ensure date is converted to datetime for grouping
        transactions = st.session_state.transactions.copy()
        transactions['date'] = pd.to_datetime(transactions['date'])  # Convert to datetime

        # Filter for 'debit' transactions and group by category
        category_spending = transactions[transactions['type'] == 'debit'] \
            .groupby('category')['amount'].sum()

        fig = px.pie(
            values=category_spending.values,
            names=category_spending.index,
            title="Category Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Weekly Spending Trend")
        # Group transactions by week
        weekly_spending = transactions[transactions['type'] == 'debit'] \
            .groupby(pd.Grouper(key='date', freq='W'))['amount'].sum().reset_index()

        fig = px.line(
            weekly_spending,
            x='date',
            y='amount',
            title="Weekly Spending Pattern"
        )
        st.plotly_chart(fig, use_container_width=True)
