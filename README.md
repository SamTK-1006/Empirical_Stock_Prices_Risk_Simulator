Quantitative Finance Dashboard: Empirical Time Series Analysis and Monte Carlo Simulation


> Overview:

A Streamlit dashboard that analyzes a stock's price history, compares its returns with a normal distribution, and simulates future price paths to estimate the risk of loss.


> Features:
 - Calculation of returns
 - Statistical analysis (mean and variance)
 - Histogram with normal distribution overlay
 - Q-Q plot for normality testing
 - Monte Carlo simulation of price paths and risk of loss


> Project Structure:

 - main.py                          : page setup, navigation and the sidebar ticker input
 - pages/                           : Home, Time Series Analysis, Distribution Analysis, Monte Carlo Simulations
 - Phase_1_Empirical_Time_Series.py : data loading, returns, statistics, price and returns plots
 - Phase_2_Distribution.py          : normal distribution overlay and Q-Q plot
 - Phase_3_Monte_Carlo.py           : simulator, risk of loss and plots


> Usage:

    pip install -r requirements.txt
    streamlit run main.py


> Summary:

This project takes the last three years of daily prices for a ticker (using yfinance) and computes returns to study their statistical properties. It evaluates whether the returns follow a normal distribution using visual methods. Based on these statistics, a Monte Carlo simulation generates possible future price paths, providing a simple probabilistic view of how the stock might move over time.


> Concepts:

Time series analysis, return distributions, normality testing, and Monte Carlo simulation.


> Libraries Used:

 - streamlit
 - numpy
 - pandas
 - scipy
 - plotly
 - yfinance


> Author:

Samarth T K
