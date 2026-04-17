# app.py
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="SupportFlow AI", layout="wide")

# ---------------------------
# Sample Ticket Data
# ---------------------------
data = {
    "Category": ["Billing", "Technical", "Account Access", "Refund", "Bug Report"],
    "Tickets": [120, 210, 80, 55, 95]
}
df = pd.DataFrame(data)

# ---------------------------
# Rules-Based Classifier
# ---------------------------
def classify_ticket(text):
    text = text.lower()

    if any(word in text for word in ["payment", "invoice", "charged", "billing"]):
        return "Billing", "High"
    elif any(word in text for word in ["password", "login", "locked", "access"]):
        return "Account Access", "High"
    elif any(word in text for word in ["refund", "cancel", "money back"]):
        return "Refund", "Medium"
    elif any(word in text for word in ["error", "bug", "issue", "not working"]):
        return "Bug Report", "Medium"
    elif any(word in text for word in ["down", "website", "domain", "plugin"]):
        return "Technical", "High"
    else:
        return "General Inquiry", "Low"

# ---------------------------
# AI Reply Generator
# ---------------------------
def generate_reply(category):
    replies = {
        "Billing": "Hello, thank you for contacting us. We are reviewing your billing concern and will assist shortly.",
        "Technical": "We understand the technical issue. Our support team is checking it now and will update you soon.",
        "Account Access": "We’re sorry you're unable to access your account. Please try resetting your password while we investigate.",
        "Refund": "We have received your refund request and our billing team is reviewing it.",
        "Bug Report": "Thank you for reporting this issue. Our product team has been notified.",
        "General Inquiry": "Thank you for reaching out. We’ll get back to you shortly."
    }
    return replies.get(category, replies["General Inquiry"])

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("SupportFlow AI")
page = st.sidebar.radio("Navigation", ["Home", "Ticket Classifier", "Dashboard", "About"])

# ---------------------------
# Home
# ---------------------------
if page == "Home":
    st.title("🚀 SupportFlow AI")
    st.subheader("AI-Powered Customer Support Optimization System")

    st.write("""
    Reduce support response time, classify tickets automatically, route urgent issues,
    and improve customer satisfaction.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Weekly Tickets", "1,800")
    col2.metric("Current Response Time", "11 Hours")
    col3.metric("Target Response Time", "1.5 Hours")

# ---------------------------
# Ticket Classifier
# ---------------------------
elif page == "Ticket Classifier":
    st.title("🎯 AI Ticket Classifier")

    ticket = st.text_area("Enter Customer Ticket")

    if st.button("Analyze Ticket"):
        if ticket.strip():
            category, priority = classify_ticket(ticket)
            reply = generate_reply(category)

            st.success("Analysis Complete")

            st.write(f"**Category:** {category}")
            st.write(f"**Priority:** {priority}")
            st.write("**Suggested First Reply:**")
            st.info(reply)
        else:
            st.warning("Please enter ticket text.")

# ---------------------------
# Dashboard
# ---------------------------
elif page == "Dashboard":
    st.title("📊 Support Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("CSAT Score", "91%")
    col2.metric("Resolved Today", "245")
    col3.metric("High Priority Open", "17")

    st.subheader("Tickets by Category")
    st.bar_chart(df.set_index("Category"))

    st.subheader("Daily Response Time Trend")
    trend = pd.DataFrame({
        "Hours": [11, 9, 7, 5, 3, 2, 1.5]
    })
    st.line_chart(trend)

# ---------------------------
# About
# ---------------------------
elif page == "About":
    st.title("📌 About Project")

    st.write("""
    **Project Name:** SupportFlow AI
    
    **Purpose:**  
    Designed to solve real SaaS support team problems using AI automation.

    **Features:**  
    - Ticket Classification  
    - Priority Detection  
    - Suggested Replies  
    - Analytics Dashboard

    **Tech Stack:**  
    Python, Streamlit, Pandas

    **Built in 3 Days as Proof of Work**
    """)
