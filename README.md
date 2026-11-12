Empirical Time Series Analysis and Monte Carlo Simulation


> Overview:

This project analyzes financial time series data using statistical methods and Monte Carlo simulation. It focuses on return distributions, normality assessment, and simulation of future price paths.


> Features:
 - Calculation of returns
 - Statistical analysis (mean and variance)
 - Histogram with normal distribution overlay
 - Q-Q plot for normality testing
 - Monte Carlo simulation of price paths (Geometric Brownian Motion, Standard, Bootstrapping)
 - Comparison of the three models and their estimated risk of loss


> Project Structure:

 - main.py                          : menu and entry point
 - Phase_1_Empirical_Time_Series.py : data loading, returns, statistics, price and returns plots
 - Phase_2_Distribution.py          : normal distribution overlay and Q-Q plot
 - Phase_3_Monte_Carlo.py           : GBM, Standard and Bootstrapping simulators, risk of loss, plots and model comparison


> Usage:

Install the dependencies and run the script:

    pip install -r requirements.txt
    python main.py


> Summary:

This project downloads the last three years of daily prices for a ticker (using yfinance) and computes returns to study their statistical properties. It evaluates whether the returns follow a normal distribution using visual and quantitative methods. Based on these statistics, Monte Carlo simulations are used to generate possible future price paths, providing a simple probabilistic view of how the stock might move over time.


> Concepts:

Time series analysis, return distributions, normality testing, and Monte Carlo simulation.


> Libraries Used:

 - numpy
 - pandas
 - matplotlib
 - scipy
 - yfinance


> Author:

Samarth T K
