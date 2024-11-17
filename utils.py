# data/utils.py

# Sample data structure for app_data (adjust it according to your actual app structure)
app_data = {
    "account_balances": {
        "user_1": 100.0,
        "user_2": 200.0
    },
    "users": [
        {"id": "user_1", "name": "Alice"},
        {"id": "user_2", "name": "Bob"}
    ]
}

def update_account_balance(user_id, new_balance):
    # Example of updating account balance
    if user_id in app_data["account_balances"]:
        app_data["account_balances"][user_id] = new_balance
