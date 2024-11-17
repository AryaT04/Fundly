import streamlit as st
from datetime import datetime


def initialize_data():
    """
    Initializes session state variables for the application.
    This function will set up initial data and ensure that the necessary session state attributes are available.
    """
    if "account_balances" not in st.session_state:
        st.session_state.account_balances = {
            1: 1000.00,  # Initial balance for user ID 1
            2: 500.00,  # Initial balance for user ID 2
        }

    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    if "insights" not in st.session_state:
        st.session_state.insights = [
            {"metric": "total_revenue", "value": 74.65},
            {"metric": "total_users", "value": 2},
        ]


def update_account_balance(user_id, deposit_amount):
    """
    Updates the account balance for a given user ID in the session state.
    Also adds a transaction record to the transactions list in the session state.
    """
    if deposit_amount <= 0:
        return False  # Deposit amount must be positive

    # Ensure session state has been initialized
    if "account_balances" not in st.session_state:
        st.session_state.account_balances = {}

    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    # Update the user's account balance
    if user_id in st.session_state.account_balances:
        st.session_state.account_balances[user_id] += deposit_amount

        # Add a record to the transactions list
        new_transaction = {
            "id": len(st.session_state.transactions) + 1,
            "user_id": user_id,
            "amount": deposit_amount,
            "date": datetime.now().strftime("%Y-%m-%d"),  # Use the current date
        }
        st.session_state.transactions.append(new_transaction)

        return True
    else:
        return False  # User not found
