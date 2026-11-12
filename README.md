# Quantitative Finance Dashboard: Empirical Time Series Analysis and Monte Carlo Simulation

## Overview

A Streamlit dashboard that analyzes a stock's price history, compares its returns with a normal distribution, and simulates future price paths to estimate the risk of loss.

This project analyzes financial time series data using statistical methods and Monte Carlo simulation, focusing on return distributions, normality assessment, and probabilistic modelling of future stock prices.

**Live Application:** [Monte Carlo Simulator](https://monte-carlo-simulator-samtk-1006.streamlit.app/)

## Features

- Calculation and analysis of stock returns
- Statistical analysis (mean and variance)
- Histogram with normal distribution overlay
- Q-Q plot for normality testing
- Monte Carlo simulation of future price paths
- Estimation of risk of loss

## Project Structure

- `main.py` — Page setup, navigation and sidebar ticker input
- `pages/` — Home, Time Series Analysis, Distribution Analysis and Monte Carlo Simulations
- `Phase_1_Empirical_Time_Series.py` — Data loading, returns, statistics, price and returns plots
- `Phase_2_Distribution.py` — Normal distribution overlay and Q-Q plot
- `Phase_3_Monte_Carlo.py` — Simulator, risk of loss and plots
- `.streamlit/config.toml` — Streamlit configuration

## Usage

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run main.py
```

## Summary

The project takes the last three years of daily prices for a selected ticker using Yahoo Finance (`yfinance`) and computes returns to study their statistical properties. It evaluates whether returns follow a normal distribution using visual methods. Based on these statistics, Monte Carlo simulations generate possible future price paths, providing a probabilistic perspective on potential stock movements.

## Concepts

- Financial Time Series Analysis
- Return Distributions
- Statistical Normality Testing
- Monte Carlo Simulation
- Probabilistic Risk Estimation

## Libraries Used

- Streamlit
- NumPy
- Pandas
- Matplotlib
- SciPy
- Plotly
- yfinance

## Author

Samarth T K
