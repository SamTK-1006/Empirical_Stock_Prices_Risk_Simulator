import Phase_1_Empirical_Time_Series as P1
import Phase_3_Monte_Carlo as P3
import numpy as np
import matplotlib.pyplot as plt

def Monte_Carlo_Simulations(data):
    P0 = data.iloc[0].values[0]
    P = data.iloc[-1].values[0]
    simulated_paths = simulator(data)
    Plot_Monte_Carlo(simulated_paths)
    print(f"Estimated Risk of Loss: {Risk_Calculation(simulated_paths, P):.2f}%\n")

# To simulate the price paths using Geometric Brownian Motion (GBM) model
def simulator(data):
    # Calculating Base Price, Mean and Variance of Returns
    returns = P1.cal_returns(data)
    returns.rename(columns={returns.columns[0]: 'Returns'}, inplace=True)
    P0 = data.iloc[0].values[0]
    P = data.iloc[-1].values[0]
    mean, var = P1.cal_stats(P1.cal_returns(data))
    mu = mean*252
    sigma = var**0.5 * (252**0.5)

    # Simulating 1000 paths for 756 trading days (3 years)
    simulated_paths = []
    for _ in range(1000):
        path = [P]
        simulated_returns = np.random.normal(0,1,756)   
        for r in simulated_returns:
            path.append(path[-1] * np.exp((mu - 0.5*sigma**2)/252 + sigma*r/(252**0.5)))
        simulated_paths.append(path)
    return simulated_paths

def Plot_Monte_Carlo(simulated_paths):
    _, (a1, a2) = plt.subplots(2,1, figsize=(10,8))

    # Plotting 100 simulated paths to visualize the price evolution
    for path in simulated_paths[:100]:
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
    a2.set_title("Monte Carlo Histogram of Final Prices", fontweight="bold")
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
    plt.show()
    
def Risk_Calculation(simulated_paths, P):
    # Calculating the risk of loss (final price < initial price)
    count = 0
    for path in simulated_paths:
        if path[-1] < P:
            count = count + 1
    risk = count / len(simulated_paths)
    return risk*100

def Comparison_of_Models(data):
    # Simulating paths using both GBM and Standard Monte Carlo models
    simulated_paths_gbm = simulator(data)
    simulated_paths_standard = P3.simulator(data)

    # Plotting the results for comparison
    _, (a1, a2) = plt.subplots(2,1, figsize=(10,8))

    # Plotting GBM Monte Carlo Paths
    # Finding the last price of each simulated path 
    last_prices_gbm = []
    for path in simulated_paths_gbm:
        last_prices_gbm.append(path[-1])

    # Labelling the axes and title
    a1.hist(last_prices_gbm, bins=50, edgecolor="black", color="purple")
    a1.set_xlabel("Final Price", fontweight="bold")
    a1.set_ylabel("Frequency", fontweight="bold")
    a1.set_title("Monte Carlo Histogram of Final Prices - Geometric Brownian Motion", fontweight="bold")
    a1.set_facecolor("lightgray")

    # Highlighting the starting price on the plot
    starting_price = simulated_paths_gbm[0][0]
    a1.text(0.985, 0.95, f"Starting Price: {starting_price:.2f}", transform = a1.transAxes, ha = "right", va = "top", fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))
    
    # Highlighting the most probable final price (mode) on the plot
    counts, bins = np.histogram(last_prices_gbm, bins=50)
    max_bin_index = np.argmax(counts)
    highest_probability_price = (bins[max_bin_index] + bins[max_bin_index+1]) / 2
    a1.text(0.985, 0.83, f"Most Probable Final Price: {highest_probability_price:.2f}", transform = a1.transAxes, ha = "right", va = "top", fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

    # Plotting Standard Monte Carlo Paths Histogram
    # Finding the last price of each simulated path 
    last_prices_standard = []
    for path in simulated_paths_standard:
        last_prices_standard.append(path[-1])

    # Labelling the axes and title
    a2.hist(last_prices_standard, bins=50, edgecolor="black", color="purple")
    a2.set_xlabel("Final Price", fontweight="bold")
    a2.set_ylabel("Frequency", fontweight="bold")
    a2.set_title("Monte Carlo Histogram of Final Prices - Standard Model", fontweight="bold")
    a2.set_facecolor("lightgray")

    # Highlighting the starting price on the plot
    starting_price = simulated_paths_standard[0][0]
    a2.text(0.985, 0.95, f"Starting Price: {starting_price:.2f}", transform = a2.transAxes, ha = "right", va = "top", fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))
    
    # Highlighting the most probable final price (mode) on the plot
    counts, bins = np.histogram(last_prices_standard, bins=50)
    max_bin_index = np.argmax(counts)
    highest_probability_price = (bins[max_bin_index] + bins[max_bin_index+1]) / 2
    a2.text(0.985, 0.83, f"Most Probable Final Price: {highest_probability_price:.2f}", transform = a2.transAxes, ha = "right", va = "top", fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

    plt.tight_layout()
    plt.show()

    # Comparing Risk of Loss for both models
    print(f"Risk of Loss for GBM: {Risk_Calculation(simulated_paths_gbm, starting_price):.2f}%")
    print(f"Risk of Loss for Standard Monte Carlo: {Risk_Calculation(simulated_paths_standard, starting_price):.2f}%\n")
