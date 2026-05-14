import Phase_1_Empirical_Time_Series as P1
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def Monte_Carlo_Simulations(data):
    # Calculating Base Price, Mean and Variance of Returns
    returns = P1.cal_returns(data)
    returns.rename(columns={returns.columns[0]: 'Returns'}, inplace=True)
    P0 = data.iloc[0].values[0]
    mean, var = P1.cal_stats(P1.cal_returns(data))

    # Simulating 1000 paths for 756 trading days (3 years)
    simulated_paths = []
    number_simulations = st.slider("Number of Simulations", min_value=100, max_value=5000, value=1000, step=100)
    for _ in range(number_simulations):
        path = [P0]
        simulated_returns = np.random.normal(mean, var**0.5, 756)
        for r in simulated_returns:
            path.append(path[-1] * np.exp(r))
        simulated_paths.append(path)
    
    Plot_Monte_Carlo(simulated_paths)
    Risk_Calculation(simulated_paths, P0)
    

def Plot_Monte_Carlo(simulated_paths):
    fig, (a1, a2) = plt.subplots(2,1, figsize=(10,8))

    # Plotting 10% simulated paths to visualize the price evolution
    for path in simulated_paths[:int(0.1 * len(simulated_paths))]:
        a1.plot(path, color="gray", alpha=0.2)
    a1.set_title("Monte Carlo Simulation of Price Paths", fontweight="bold")
    a1.set_xlabel("Days", fontweight="bold")
    a1.set_ylabel("Price", fontweight="bold")
    a1.set_facecolor("lightgray")
    
    # Finding the last price of each simulated path 
    last_prices = []
    for path in simulated_paths:
        last_prices.append(path[-1])

    # Labelling the axes and title
    a2.hist(last_prices, bins=50, edgecolor="black", color="purple")
    a2.set_xlabel("Final Price", fontweight="bold")
    a2.set_ylabel("Frequency", fontweight="bold")
    a2.set_title("Histogram of Final Prices", fontweight="bold")
    a2.set_facecolor("lightgray")

    # Highlighting the starting price on the plot
    starting_price = simulated_paths[0][0]
    a2.text(0.985, 0.95, f"Starting Price: {starting_price:.2f}", transform = a2.transAxes, ha = "right", va = "top", fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))
    
    # Highlighting the most probable final price (mode) on the plot
    counts, bins = np.histogram(last_prices, bins=50)
    max_bin_index = np.argmax(counts)
    highest_probability_price = (bins[max_bin_index] + bins[max_bin_index+1]) / 2
    a2.text(0.985, 0.83, f"Most Probable Final Price: {highest_probability_price:.2f}", transform = a2.transAxes, ha = "right", va = "top", fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))
    
    plt.tight_layout()
    st.pyplot(fig)

def Risk_Calculation(simulated_paths, P0):
    # Calculating the risk of loss (final price < initial price)
    count = 0
    for path in simulated_paths:
        if path[-1] < P0:
            count = count + 1
    risk = count / len(simulated_paths)
    st.subheader(f"Risk of Loss: {risk:.2%}")

