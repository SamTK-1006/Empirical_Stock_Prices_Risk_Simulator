import streamlit as st
import Phase_1_Empirical_Time_Series

# Setting up the Streamlit title
st.title("Empirical Time Series Analysis")
data = st.session_state.get("data")

# Introduction and to Empirical Time Series Analysis
st.markdown("""
This section explores the historical behavior of a stock price
through empirical time series analysis.

The objective is to understand:
- how the price evolves over time,
- how returns behave statistically,
- and whether the return distribution resembles a normal distribution.
---
""")

# Visualization of Price Time Series and Returns
st.subheader("Price Time Series and Returns Visualization")
if data is not None:
    Phase_1_Empirical_Time_Series.use_yahoo(data)
else:
    st.write("Please enter a ticker symbol in the main page to view the time series analysis.")

st.divider()

# Explanation of the Graphs and Statistics
st.subheader("""
        Explanation of the Graphs and Statistics
            """)

with st.expander("Price Time Series"):
    st.markdown("""
The first graph displays the historical price path of the selected asset.

A time series is a sequence of observations recorded over time.
In finance, the price time series helps visualize:
- long-term trends,
- volatility,
- market shocks,
- and periods of rapid growth or decline (extreme events).

The closing price is commonly used because it represents the
final market consensus price for a trading day.
""")

with st.expander("Returns"):
    st.markdown("""
Raw prices are generally not suitable for statistical modeling
because they are non-stationary and depend heavily on scale.

Instead, financial analysis is usually performed using returns.

The simple return is calculated as:

""")
    st.latex(r"R_t = \frac{P_t - P_{t-1}}{P_{t-1}}")
    st.markdown(r"""

where:

- $$(P_t$$) = current price
- $$(P_{t-1}$$) = price of the previous period
- $$(R_t$$) = return at time \(t\)

Returns measure the percentage change in price between two periods. So, if the price was 100 yesterday and 101 today, the returns would be +0.01 (or +1%). If the price drops to 99, the returns would be -0.01 (or -1%).
""")

with st.expander("Returns Histogram"):
    st.markdown("""
The second graph displays the return histogram.

Unlike prices, returns fluctuate around a relatively stable mean
and are more suitable for statistical analysis and modeling.

The return histogram is useful for studying:
- volatility,
- distribution behavior,
- extreme events,
- and randomness in financial markets.

Large spikes in the return series often correspond to
major market events or periods of uncertainty.
""")

with st.expander("Statistical Measures"):
    st.markdown("""
The analysis also includes key statistical quantities:
""")
    with st.expander("Mean Returns"):
        st.markdown("""
### Mean Return

The average return over the observed period:

""")
        st.latex(r"\mu = \frac{1}{n}\sum_{i=1}^{n} R_i")
        st.markdown("""

The mean return provides an estimate of the asset's
average growth rate.
""")

    with st.expander("Variance"):
        st.markdown("""
Variance measures the dispersion of returns around the mean:

""")
        st.latex(r"\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(R_i - \mu)^2")
        st.markdown("""
Higher variance indicates greater uncertainty and volatility.
    """)

    with st.expander("Standard Deviation"):
        st.markdown("""
The standard deviation is the square root of variance:

""")
        st.latex(r"\sigma = \sqrt{\sigma^2}")
        st.markdown("""

Standard deviation is one of the most widely used
risk measures in quantitative finance.

A larger standard deviation implies larger fluctuations in returns
and therefore higher risk.
""")
    
# Conclusion of the Empirical Time Series Analysis
st.markdown("""
We will analyze the returns of the stock prices in the following section to understand their statistical properties to further model simulations.""")
