import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import streamlit as st

def use_yahoo(data):
    # Plotting the Price and Returns
    data_plot(data)

    # Printing mean and variance of returns
    mean, var = cal_stats(cal_returns(data))
    col1, col2, col3 = st.columns([2,2,1])
    with col1:  
        st.metric("Mean Return", f"{mean:.6f}")
    with col2:
        st.metric("Return Std Dev", f"{np.sqrt(var):.6f}")
    with col3:
        st.metric("Return Variance", f"{var:.6f}")

def cal_returns(data):                                 
    # Calculates the Returns
    returns = np.log(data/data.shift(1))
    return returns.dropna()

def cal_stats(data):
    # Calculates the Mean and Variance of the Returns
    return data.mean().item(), data.var().item()

def data_plot(data):
    # Plots the Price and Returns
    fig, (a1, a2) = plt.subplots(2,1, figsize=(10,6))

    a1.plot(data, linewidth= 2, color = "blue")
    a1.set_title("Close Price", fontweight="bold")
    a1.set_xlabel("Date", fontweight="bold")
    a1.set_ylabel("Price", fontweight="bold")
    a1.set_facecolor("lightgray")

    a2.hist(cal_returns(data), color = "orange", edgecolor = "black", bins = 20)
    a2.set_title("Returns", fontweight="bold")
    a2.set_xlabel("Return Values", fontweight="bold")
    a2.set_ylabel("Frequency", fontweight="bold")
    a2.set_facecolor("lightgray")
    
    plt.tight_layout()
    st.pyplot(fig)


