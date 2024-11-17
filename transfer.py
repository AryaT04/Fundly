import streamlit as st

# Transfer Page Logic
def transfer_page():
    # Initialize 'accounts' in session_state if it doesn't exist
    if "accounts" not in st.session_state:
        st.session_state.accounts = {
            "Account 1": 1000.00,  # Example account balances
            "Account 2": 500.00,
            "Account 3": 250.00
        }

    st.title("Transfer Money")

    # Amount input field
    transfer_amount = st.number_input("Enter transfer amount:", min_value=0.01, step=0.01)

    # Account to transfer from
    source_account = st.selectbox(
        "Select account to transfer from:",
        list(st.session_state.accounts.keys())
    )

    # Account to transfer to
    destination_account = st.selectbox(
        "Select account to transfer to:",
        [acc for acc in st.session_state.accounts.keys() if acc != source_account]
    )

    # Transfer button
    if st.button("Transfer"):
        # Check if the source account has enough balance
        if st.session_state.accounts[source_account] >= transfer_amount:
            # Perform the transfer
            st.session_state.accounts[source_account] -= transfer_amount
            st.session_state.accounts[destination_account] += transfer_amount

            # Display success message
            st.success(f"Successfully transferred ${transfer_amount:.2f} to {destination_account}'s account!")

            # Show remaining balance for the source account
            st.write(f"Remaining Balance of {source_account}: ${st.session_state.accounts[source_account]:.2f}")
        else:
            # Display error if insufficient balance
            st.error(f"Insufficient balance in {source_account}. Transfer cannot be completed.")


# Call the transfer page function
transfer_page()
