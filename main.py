import Phase_1_Empirical_Time_Series
import Phase_2_Distribution
import Phase_3_Monte_Carlo
import yfinance as yf
import streamlit as st

def main():
    st.title("Empirical Time Series Analysis")
 
    ticker = st.text_input("Enter the ticker symbol (e.g., AAPL): ").strip()
    if ticker: 
        data = yf.download(ticker, period = "3y", interval = "1d")["Close"].dropna()
        Phase_1_Empirical_Time_Series.use_yahoo(data)
        
    # Distribution Analysis
    st.title("Distribution Analysis")
    # Using session state to toggle the display of distribution analysis when the button is clicked
    if "show_dist" not in st.session_state:
        st.session_state.show_dist = False
    if st.button("Show Distribution Analysis"):
        st.session_state.show_dist = not st.session_state.show_dist
    if st.session_state.show_dist:
        Phase_2_Distribution.distribution_ticker(data)
    
    # Using session state to toggle the display of Q-Q plot when the button is clicked
    if "show_qq" not in st.session_state:
        st.session_state.show_qq = False
    if st.button("Show Q-Q Plot"):
        st.session_state.show_qq = not st.session_state.show_qq
    if st.session_state.show_qq:
        Phase_2_Distribution.generate_qq(data)

    # Monte Carlo Simulations
    st.title("Monte Carlo Simulations")
    # Using session state to toggle the display of Monte Carlo simulations when the button is clicked
    if "show_mc" not in st.session_state:
        st.session_state.show_mc = False
    if st.button("Run Monte Carlo Simulations"):
        st.session_state.show_mc = not st.session_state.show_mc
    if st.session_state.show_mc:
        Phase_3_Monte_Carlo.Monte_Carlo_Simulations(data)
    
if __name__ == "__main__":    
    main()
