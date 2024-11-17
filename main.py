import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

currentBalance = 3211.43
userName = "Jane Doe"
totalIncome = 0


# Sample data 
user_data = {
    "name": "John Doe",
    "balance": 3450.75,
    "transactions": [
        {"date": "2024-11-15", "description": "Groceries", "amount": -1150.45},
        {"date": "2024-11-14", "description": "Salary", "amount": 1500.00},
        {"date": "2024-11-13", "description": "Electric Bill", "amount": 120.25},
        {"date": "2024-11-12", "description": "Transfer to Savings", "amount": -200.00},
        {"date": "2024-11-11", "description": "Food", "amount": -4.50},
        {"date": "2024-11-11", "description": "Food", "amount": -10.50},
    ],
    "spending_goals": 5000,  # Goal for savings or spending limit
}

st.set_page_config(layout="wide")
# Adjust columns to have equal proportions
col1, col2, col3 = st.columns([1, 1, 1])

# Ensure the card styling is consistent
st.markdown(
    """
    <style>
    .card {
        border: 2px solid #2f5d30; /* Green border */
        padding: 20px;
        border-radius: 10px;
        background-color: #f5f5f5;
        text-align: center; /* Center content for uniformity */
        height: 150px; /* Fixed height for uniformity */
    }

    .green-card {
        background-color: #2f5d30; /* Dark green background */
        color: white;
    }

    /* Ensures consistent box sizing */
    .stColumn > div {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Hello User Button
with col1:
    st.markdown(
        f"""
        <div class="card green-card" style="text-align: left; padding-left: 20px;">
            <h3 style="color: white; margin: 0;">Good morning,</h3>
            <h3 style="color: white; margin: 0;">{userName}</h3>
        </div>
        """,
        
        unsafe_allow_html=True,
    )

    

   
   
    


# display current balance 
with col2:
    st.markdown(
        f"""
        <div class="card">
            <h3 style="margin: 0;">Current Balance</h3>
            <h2>${currentBalance}</h2> 
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Add padding between the cards
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    st.markdown(
        f"""
        <div class="card" style="padding: 20px; background-color: white; border-radius: 10px; border: 2px solid #2f5d30;height: 330px;">
            <h3 style="margin: 0;">Personal Insights</h3>
            <p style = "text-align: left">Total income this month: {sum([txn['amount'] for txn in user_data["transactions"] if txn['amount'] > 0])} <p>
            <p style = "text-align: left">Total expenses this month: {-1*(sum([txn['amount'] for txn in user_data["transactions"] if txn['amount'] < 0]))}<p>
            <p style = "text-align: left">Average spending per transaction: {-1*(np.mean([txn['amount'] for txn in user_data["transactions"] if txn['amount'] < 0])):.2f}<p>
    
        </div>
        """,
        unsafe_allow_html=True,
    )

    

# Function for fraud detection
def fraud_detection(transactions):
    # Example of basic fraud detection: flagging any large transactions
    alerts = []
    for txn in transactions:
        if txn['amount'] < -1000:
            alerts.append(f"Alert: {txn['description']} - ${txn['amount']}")
    return alerts


with col3:
    # Display fraud detection alerts dynamically inside the card
    fraud_alerts = fraud_detection(user_data["transactions"])  # Assuming fraud_detection is defined

    # Build the card with dynamic content
    alert_content = ""
    if fraud_alerts:
        for alert in fraud_alerts:
            alert_content += f'<p style="color: brown; background-color: #fff9e6; padding: 10px; border-radius: 5px;">⚠️ {alert}</p>'
    else:
        alert_content = '<p style="color: green;">✅ No unusual transactions detected.</p>'

    # Render the Fraud Detection card
    st.markdown(
        f"""
        <div class="card" style="padding: 20px; background-color: white; border-radius: 10px; border: 2px solid #2f5d30;">
            <h3 style="margin: 0;">Fraud Detection</h3>
            {alert_content}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Add padding between the cards
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
     
    
    # Display recent transactions
    transaction_df = pd.DataFrame(user_data["transactions"])
    transaction_df = transaction_df.reset_index(drop=True)
    # Render the Recent Transactions card with extended height
    st.markdown(
        f"""
        <h3 style="margin: 0;text-align: center;">Recent Transactions</h3>
        """,
        unsafe_allow_html=True,
    )

    # Place the transactions table inside the card
    st.dataframe(transaction_df, use_container_width=True)
























# Run a plot of spending over time
st.subheader("Spending Over Time")
transaction_df['date'] = pd.to_datetime(transaction_df['date'])
transaction_df['cumulative_spending'] = transaction_df['amount'].cumsum()
fig, ax = plt.subplots()
ax.plot(transaction_df['date'], transaction_df['cumulative_spending'], marker='o')
ax.set_title('Cumulative Spending Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Amount ($)')
st.pyplot(fig)

