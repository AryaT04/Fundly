import streamlit as st
from datetime import datetime, timedelta
import pandas as pd


def calculate_metrics():
    # Check if transactions exist and are a valid DataFrame
    if 'transactions' not in st.session_state or not isinstance(st.session_state.transactions, pd.DataFrame):
        return {}  # Handle case if no transactions or invalid DataFrame

    df = st.session_state.transactions

    # Handle case where the DataFrame is empty
    if df.empty:
        return {}

    # Filter transactions for the last 30 days
    recent_df = df[df['date'] >= (datetime.now() - timedelta(days=30))]

    # Calculate metrics
    total_spending = recent_df[recent_df['type'] == 'debit']['amount'].sum()
    avg_daily_spending = recent_df[recent_df['type'] == 'debit']['amount'].mean()

    # Handle case where there are no debit transactions
    top_category = None
    if not recent_df[recent_df['type'] == 'debit'].empty:
        top_category = recent_df[recent_df['type'] == 'debit']['category'].mode().iloc[0]

    # Calculate monthly savings (credit - debit)
    monthly_savings = recent_df[recent_df['type'] == 'credit']['amount'].sum() - \
                      recent_df[recent_df['type'] == 'debit']['amount'].sum()

    # Return metrics
    metrics = {
        'total_spending': total_spending,
        'avg_daily_spending': avg_daily_spending,
        'top_category': top_category,
        'monthly_savings': monthly_savings
    }

    return metrics
