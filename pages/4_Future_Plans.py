import streamlit as st

# Setting up the Streamlit title
st.title("What's Next for the Project?")

# Future Plans and Extensions
with st.expander("Multi-asset Monte Carlo Simulation"):
    st.write("""
    Simulating multiple assets simultaneously to analyze portfolio-level behavior
    and interactions between different securities.
    """)

with st.expander("Stochastic Process Modeling in Finance"):
    st.write("""
    Applying mathematical random processes to model uncertainty, volatility,
    and time-dependent dynamics in financial markets.
    """)

with st.expander("Portfolio Risk and Return Modeling"):
    st.write("""
    Studying how combinations of assets behave together in terms of expected
    returns, diversification, and overall portfolio risk.
    """)

with st.expander("Correlation and Covariance Matrix Analysis"):
    st.write("""
    Measuring relationships between assets to understand how their price movements
    are related under different market conditions.
    """)

with st.expander("Factor Models and Principal Component Analysis (PCA)"):
    st.write("""
    Identifying the major underlying factors that drive market movements and
    reducing complex financial datasets into key components.
    """)

with st.expander("Geometric Brownian Motion (GBM) Extensions"):
    st.write("""
    Enhancing the current simulation framework using more advanced stochastic
    models and improved assumptions about market behavior.
    """)

with st.expander("Value at Risk (VaR) and Advanced Risk Metrics"):
    st.write("""
    Estimating the probability and magnitude of potential losses under different
    market scenarios and volatility conditions.
    """)

st.divider()