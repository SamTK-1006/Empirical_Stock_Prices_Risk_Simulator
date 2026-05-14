import Phase_1_Empirical_Time_Series as P1
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sc
import streamlit as st

def distribution_ticker(data):
    # Comparing distribution of returns with normal distribution
    returns = P1.cal_returns(data)
    mean, var = P1.cal_stats(returns)
    
    # Plotting the original histogram of returns
    fig , ax = plt.subplots(figsize=(10,6))
    ax.hist(returns, color = "orange", edgecolor = "black", bins = 20, density = True)
    ax.set_title("Normal Distribution Overlay", fontweight="bold")
    ax.set_xlabel("Return Values", fontweight="bold")
    ax.set_ylabel("Density", fontweight="bold")
    ax.set_facecolor("lightgray")

    # Plotting normal distribution overlay
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 10000)
    p = sc.norm.pdf(x, mean, var**0.5)
    ax.plot(x, p, "black" , linewidth=1.5)

    plt.tight_layout()
    st.pyplot(fig)

def generate_qq(data):
    # Q-Q plot to compare empirical returns with theoretical normal distribution

    # Calulating empirical returns and statistics
    returns = P1.cal_returns(data).dropna()
    mean, var = P1.cal_stats(returns)
    returns = np.sort(returns)
    returns = sorted(returns)

    # Generating theoretical quantiles
    theoretical = sc.norm.ppf(np.linspace(1/len(returns), (len(returns)-1)/len(returns), len(returns)), loc=mean, scale=var**0.5)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(theoretical, returns, color = "blue", marker = "o", linestyle="None")
    ax.plot(theoretical, theoretical, color = "red", linestyle="--")
    
    # Setting limits to ensure the plot is square and properly scaled
    min_val = min(theoretical.min(), min(returns))
    max_val = max(theoretical.max(), max(returns))
    ax.set_xlim(min_val, max_val)
    ax.set_ylim(min_val, max_val)

    # Adding labels and title
    ax.set_xlabel("Theoretical Quantiles", fontweight="bold")
    ax.set_ylabel("Empirical Quantiles", fontweight="bold")
    ax.set_title("Q-Q Plot", fontweight="bold")

    plt.tight_layout()
    st.pyplot(fig)
