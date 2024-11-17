import streamlit as st

# Deposit Page Logic
def deposit_page():
    # Initialize 'accounts' in session_state if it doesn't exist
    if "accounts" not in st.session_state:
        st.session_state.accounts = {
            "Account 1": 1000.00,  # Example account balances
            "Account 2": 500.00,
            "Account 3": 250.00
        }

    st.title("Deposit Money")

    # Amount input field
    deposit_amount = st.number_input("Enter deposit amount:", min_value=0.01, step=0.01)

    # Check if deposit amount is greater than 0.00
    if deposit_amount <= 0:
        st.error("The deposit amount must be greater than 0.00.")
        return

    # Account selection (from session state)
    recipient_account = st.selectbox("Select account to deposit into:", list(st.session_state.accounts.keys()))

    # Deposit button
    if st.button("Deposit"):
        # Logic to process the deposit
        st.session_state.accounts[recipient_account] += deposit_amount

        # Display success message
        st.success(f"Deposited ${deposit_amount:.2f} successfully into {recipient_account}.")
        # Optionally display updated balance
        st.write(f"Updated Balance of {recipient_account}: ${st.session_state.accounts[recipient_account]:.2f}")


# Call the deposit page function
deposit_page()
