import yfinance as yf
import streamlit as st
import Phase_1_Empirical_Time_Series

def main():
    # Setting up the Streamlit title
    st.set_page_config(page_title = "Quantitative Finance Dashboard", layout = "wide")
    st.title("Quantitative Finance Dashboard")

    # Introduction and instructions for the user
    st.markdown("""
    Welcome to the Quantitative Finance Dashboard! This dashboard provides insights into financial data through various analyses and simulations.

    This project explores:
    - Empirical time series analysis
    - Distribution analysis
    - Q-Q plots
    - Monte Carlo simulation
                
    This project is ultimately a risk management tool that can be used to analyze the risk of a stock and its future price behavior.

    Use the sidebar to navigate between pages.
    """)
 
    # User input for ticker symbol and data fetching
    ticker = st.text_input("Enter the ticker symbol (e.g., AAPL): ").strip()
    data = None
    if ticker:
        data = yf.download(ticker, period = "3y", interval = "1d")["Close"].dropna()
        if Phase_1_Empirical_Time_Series.cal_returns(data).empty:
            data = None
            st.write("Invalid ticker symbol. Please enter a valid ticker symbol.")
        else:
            st.write("Successful! Fetching data for ticker.")
    else:
        st.write("Please enter a valid ticker symbol.")    
    st.session_state["ticker"] = ticker
    st.session_state["data"] = data
    
    st.divider()

    # Project in one sentence
    st.subheader("Project in one Sentence")
    st.write("This project analyzes the historical behaviour of a stock price, assumes the same behaviour in the future, and simulates various scenarios to estimate the risk of loss.")
if __name__ == "__main__":    
    main()
