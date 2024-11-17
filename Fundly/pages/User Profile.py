import streamlit as st
import pandas as pd
import numpy as np


def profile_page():
    st.title("Profile Page")

    # Personal Information Form
    st.subheader("Personal Information")
    with st.form("personal_info"):
        name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        phone = st.text_input("Phone Number", placeholder="Enter your phone number")

        submit_button = st.form_submit_button(label="Save Information")

        if submit_button:
            st.success("Information Saved Successfully!")
            st.write(f"Name: {name}")
            st.write(f"Email: {email}")
            st.write(f"Phone: {phone}")

    # Savings Goal Section
    st.subheader("Savings Goal")
    goal = st.number_input("Set Your Savings Goal ($)", min_value=0, step=100, value=5000)
    current_savings = st.number_input("Current Savings ($)", min_value=0, step=50, value=2000)

    # Calculate progress percentage
    if goal > 0:
        progress = (current_savings / goal) * 100
    else:
        progress = 0

    # Display savings goal progress with color coding
    if progress >= 100:
        goal_color = "green"
        progress_bar_color = "#28a745"  # Green
    elif progress >= 50:
        goal_color = "#FFB800"  # Dark Yellow
        progress_bar_color = "#FFB800"  # Dark Yellow
    else:
        goal_color = "red"
        progress_bar_color = "#dc3545"  # Red

    # Display current savings and goal with the same style
    st.markdown(
        f"### Current Savings: <span style='font-size: 28px; font-weight: 600; color:#31333F;'>{current_savings}</span> / <span style='font-size: 28px; font-weight: 600 ; color:#31333F;'>{goal}</span>",
        unsafe_allow_html=True)

    st.markdown(f"""
        <div style="background-color: #f0f0f0; border-radius: 8px; height: 30px; width: 100%;">
            <div style="width: {progress}%; height: 100%; border-radius: 8px; background-color: {progress_bar_color};">
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Cast progress to integer to display without decimal places
    progress_int = int(progress)  # Remove decimal part
    st.markdown(f"<p style='color:{goal_color}; font-size: 20px; font-weight: bold;'>Progress: {progress_int}%</p>",
                unsafe_allow_html=True)

    # Spending Percent Goals by Category
    st.subheader("Set Spending Goals by Category")

    categories = ['Food', 'Rent', 'Utilities', 'Entertainment', 'Transportation', 'Healthcare', 'Shopping']
    spending_goals = {}

    with st.form("spending_goals"):
        for category in categories:
            spending_goals[category] = st.slider(f"Set spending percentage for {category}",
                                                 min_value=0, max_value=100, value=20, step=1)

        submit_spending_button = st.form_submit_button(label="Save Spending Goals")

        if submit_spending_button:
            st.success("Spending Goals Saved Successfully!")
            # Display set spending percentages
            st.write("### Spending Goals by Category")
            for category, goal in spending_goals.items():
                st.write(f"{category}: {goal}%")

    # Display all profile info
    st.write("### Profile Information Summary")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Phone Number: {phone}")
    st.write(f"Savings Goal: ${goal}")
    st.write(f"Current Savings: ${current_savings}")

    # Allow user to download profile information as CSV (optional)
    profile_data = {
        "Name": [name],
        "Email": [email],
        "Phone": [phone],
        "Savings Goal": [goal],
        "Current Savings": [current_savings],
        "Savings Progress (%)": [progress],
    }
    profile_df = pd.DataFrame(profile_data)
    st.download_button(
        label="Download Profile Data",
        data=profile_df.to_csv(index=False),
        file_name='profile_data.csv',
        mime='text/csv'
    )




profile_page()
