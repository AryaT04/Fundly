import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")


def dashboard_page():
    currentBalance = 3211.43
    userName = "Jane Doe"
    totalIncome = 0

    logo_path = "logo.png"

    # Sample data
    user_data = {
        "name": "John Doe",
        "balance": 3450.75,
        "transactions": [
            {"date": "2024-11-15", "description": "Groceries", "amount": -150.45},
            {"date": "2024-11-14", "description": "Salary", "amount": 1500.00},
            {"date": "2024-11-13", "description": "Electric Bill", "amount": -120.25},
            {"date": "2024-11-11", "description": "Restaurant", "amount": -75.50},
            {"date": "2024-11-11", "description": "Entertainment", "amount": -100.50},
            {"date": "2024-11-11", "description": "Shopping", "amount": -1100.50},

        ],
        "spending_goals": 5000,  # Goal for savings or spending limit
    }

    # Adjust columns to have equal proportions
    tcol1, tcol2, tcol3, tcol4, tcol5, tcol6, tcol7, tcol8 = st.columns([1,1, 1, 1, 1, 1, 1, 1])
    with tcol4:
        st.image(logo_path, width=300)
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

        # Add padding between the cards
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

        # Render the Recent Transactions card with extended height
        st.markdown(
            f"""
        <h3 style="margin: 0;text-align: center;">Spending Trends</h3>
        """,
            unsafe_allow_html=True,
        )

        # Convert transactions to a DataFrame
        transactions_df = pd.DataFrame(user_data["transactions"])

        # Add a 'Category' column based on the 'description'
        def assign_category(description):
            if "groceries" in description.lower():
                return "Groceries"
            elif "entertainment" in description.lower():
                return "Entertainment"
            elif "shopping" in description.lower():
                return "Shopping"
            elif "savings" in description.lower():
                return "Savings"
            elif "restaurant" in description.lower():
                return "Restaurant"
            else:
                return "Other"

        transactions_df["Category"] = transactions_df["description"].apply(assign_category)

        # Filter only spending transactions (negative amounts)
        filtered_data = transactions_df[transactions_df["amount"] < 0]

        # Group by Category and calculate total spending
        category_spending = filtered_data.groupby("Category")["amount"].sum().reset_index()

        # Round the 'amount' column to 2 decimal places and make it positive
        category_spending["amount"] = category_spending["amount"].abs().round(2)

        # Create a pie chart using Plotly
        fig_category = px.pie(
            category_spending,
            names="Category",
            values="amount",
            color="Category",
            hole=0.3  # Creates a donut chart
        )

        # Customize hovertemplate to show values rounded to 2 decimal places
        fig_category.update_traces(hovertemplate="%{label}: %{value:.2f}<extra></extra>")

        # Display in Streamlit

        st.plotly_chart(fig_category, use_container_width=True)

    # display current balance
    with col2:
        # Current Balance Card
        st.markdown(
            f"""
            <div class="card">
                <h3 style="margin: 0;">Current Balance</h3>
                <h3 style="bold">${currentBalance}</h3> 
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Add padding between the cards
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        # Personal Insights Card
        st.markdown(
            f"""
            <div class="card" style="padding: 20px; background-color: white; border-radius: 10px; border: 2px solid #2f5d30;height: 230px;">
                <h3 style="margin: 0;">Personal Insights</h3>
                <p style = "text-align: left">Total income this month: ${sum([txn['amount'] for txn in user_data["transactions"] if txn['amount'] > 0])} <p>
                <p style = "text-align: left">Total expenses this month: ${-1 * (sum([txn['amount'] for txn in user_data["transactions"] if txn['amount'] < 0]))}<p>
                <p style = "text-align: left">Average spending per transaction: ${-1 * (np.mean([txn['amount'] for txn in user_data["transactions"] if txn['amount'] < 0])):.2f}<p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # Add padding between the cards
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        # Financial Health Score Card
        # Financial Health Score Calculation
        def calculate_financial_health(user_data, current_balance):
            # Assign weights to different components
            income_weight = 0.4
            spending_weight = 0.3
            savings_weight = 0.2
            goal_weight = 0.1

            # Calculate income health (higher income = higher score)
            total_income = sum([txn['amount'] for txn in user_data["transactions"] if txn["amount"] > 0])
            income_score = min(total_income / 5000, 1) * 100  # Normalize to a score out of 100

            # Calculate spending health (lower spending = higher score)
            total_spent = -1 * sum([txn['amount'] for txn in user_data["transactions"] if txn["amount"] < 0])
            spending_score = max(1 - total_spent / 3000, 0) * 100  # Penalize overspending

            # Calculate savings health (higher savings = higher score)
            savings_score = min(current_balance / user_data["spending_goals"], 1) * 100

            # Calculate goal progress (closer to goal = higher score)
            goal_score = min(current_balance / user_data["spending_goals"], 1) * 100

            # Weighted average
            health_score = (
                    income_weight * income_score
                    + spending_weight * spending_score
                    + savings_weight * savings_score
                    + goal_weight * goal_score
            )
            return round(health_score, 2), income_score, spending_score, savings_score, goal_score

        # Calculate the scores
        health_score, income_score, spending_score, savings_score, goal_score = calculate_financial_health(
            user_data, currentBalance
        )

        # Display the Financial Health Score dynamically in the card
        st.markdown(
            f"""
            <div class="card" style="padding: 20px; background-color: white; border-radius: 10px; border: 2px solid #2f5d30;height: 182px;">
                <h3 style="margin: 0;">Financial Health Score</h3>
                <h3 style="margin: 0;">{health_score}</h3>
            </div>
            """,

            unsafe_allow_html=True,
        )

        # Display a breakdown of scores
        # with st.expander("View Detailed Breakdown"):
        # st.write(f"**Income Score:** {income_score:.0f}/100")
        # st.write(f"**Spending Score:** {spending_score:.0f}/100")
        # st.write(f"**Savings Score:** {savings_score:.0f}/100")
        # st.write(f"**Goal Progress Score:** {goal_score:.0f}/100")

    # Function for fraud detection
    def fraud_detection(transactions):
        # Example of basic fraud detection: flagging any large transactions
        alerts = []
        for txn in transactions:
            if txn['amount'] < -1000:
                alerts.append(f"Alert: {txn['description']}   ${txn['amount']}")
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
        # Format transaction amounts to two decimal places
        transaction_df = pd.DataFrame(user_data["transactions"])
        transaction_df["amount"] = transaction_df["amount"].map("{:.2f}".format)
        transaction_df = transaction_df.reset_index(drop=True)

        def style_table(df):
            return df.style.set_table_styles(
                [
                    {"selector": "thead th",
                     "props": [("background-color", "white"), ("color", "black"), ("font-weight", "bold")]},
                    # Header styling
                    {"selector": "tbody td", "props": [("background-color", "#f9f9f9"), ("color", "black")]},
                    # Cell styling
                    {"selector": "tbody tr:hover", "props": [("background-color", "#f0f0f0")]},  # Row hover effect
                ]
            )

        # Apply the style
        styled_df = style_table(transaction_df)

        # Place the transactions table inside the styled card
        st.markdown("<h3 style='text-align: center;'>Recent Transactions</h3>", unsafe_allow_html=True)
        st.write(styled_df.to_html(), unsafe_allow_html=True)


dashboard_page()