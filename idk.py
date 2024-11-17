import streamlit as st
from pages import dashboard, deposit, savings, transfer, transactions, security, insights
from data.sample_data import initialize_data  # Import initialize_data

def profile():
    # Ensure data is initialized
    initialize_data()

    # Sidebar Navigation (Only keep necessary pages in the sidebar)
    page = st.sidebar.radio("Select a page", ("Dashboard", "Deposit", "Savings", "Transfer", "Transactions", "Security", "Insights"))

    # Page routing based on sidebar selection
    if page == "Dashboard":
        dashboard.show_dashboard()  # Show the dashboard page
    elif page == "Deposit":
        deposit.deposit_page()  # Show the deposit page
    elif page == "Savings":
        savings.savings_page()  # Show the savings page
    elif page == "Transfer":
        transfer.transfer_page()  # Show the transfer page
    elif page == "Transactions":
        transactions.show_transactions()  # Show the transactions page
    elif page == "Security":
        security.show_security()  # Show the security page
    elif page == "Insights":
        insights.show_insights()  # Show the insights page

if __name__ == "__main__":  # Changed from "__profile__" to "__main__"
    profile()
