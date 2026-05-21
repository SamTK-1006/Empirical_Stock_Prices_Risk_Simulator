import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def time_series(data):
    # Printing mean and variance of returns
    mean, var = cal_stats(cal_returns(data))
    print(f"Mean Returns: {mean}, Variance of Returns: {var}")

    # Plotting the Price and Returns
    data_plot(data) 

def cal_returns(data):                                 
    # Calculates the Returns
    returns = np.log(data/data.shift(1))
    return returns.dropna()

def cal_stats(data):
    # Calculates the Mean and Variance of the Returns
    return data.mean().item(), data.var().item()

def data_plot(data):
    # Plots the Price and Returns
    _, (a1, a2) = plt.subplots(2,1, figsize=(10,6))

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
    plt.show()


