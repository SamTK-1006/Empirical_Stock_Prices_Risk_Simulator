import streamlit as st

import Phase_1_Empirical_Time_Series as P1

st.set_page_config(page_title="Quantitative Finance Dashboard", page_icon="📈", layout="wide")

page = st.navigation([
    st.Page("pages/Home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/Time_Series_Analysis.py", title="Time Series Analysis", icon="📈"),
    st.Page("pages/Distribution_Analysis.py", title="Distribution Analysis", icon="📊"),
    st.Page("pages/Monte_Carlo_Simulations.py", title="Monte Carlo Simulations", icon="🎲"),
])

with st.sidebar:
    st.header("Stock")
    ticker = st.text_input("Ticker symbol", placeholder="e.g. AAPL").strip().upper()
    data = P1.load_data(ticker) if ticker else None

    if data is not None:
        st.success(f"{ticker} loaded: {len(data)} trading days", icon="✅")
    elif ticker:
        st.error("Invalid ticker symbol. Please enter a valid ticker symbol.", icon="🚫")
    st.divider()
    st.caption("Samarth T K")

st.session_state["ticker"], st.session_state["data"] = ticker, data
page.run()
