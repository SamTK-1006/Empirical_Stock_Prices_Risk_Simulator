import streamlit as st

st.title("📈 Quantitative Finance Dashboard")
st.write("Welcome! This dashboard provides insights into financial data through various analyses and simulations. "
         "Enter a ticker symbol in the sidebar, then use the menu to move between pages.")

st.subheader("What it covers")
st.markdown("""
- **Empirical time series analysis**: price history, returns, mean and variance
- **Distribution analysis**: normal distribution overlay and Q-Q plot
- **Monte Carlo simulation**: simulated price paths and the estimated risk of loss
""")

st.subheader("Project in one Sentence")
st.info("This project analyzes the historical behaviour of a stock price, assumes the same behaviour in the future, "
        "and simulates various scenarios to estimate the risk of loss. It is ultimately a risk management tool.")
