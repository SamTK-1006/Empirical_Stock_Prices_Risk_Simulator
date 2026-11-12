import numpy as np
import matplotlib.pyplot as plt

import Phase_1_Empirical_Time_Series as P1

# Simulating 1000 paths for 756 trading days (3 years)
N_PATHS = 1000
N_DAYS = 756
TRADING_DAYS = 252

rng = np.random.default_rng()


# ---------------------------------------------------------------- Simulators
def build_paths(P, log_returns):
    # Turns a (paths x days) array of log returns into price paths starting at P
    start = np.full((log_returns.shape[0], 1), P)
    return np.hstack([start, P * np.exp(np.cumsum(log_returns, axis=1))])


def Standard_Simulator(data):
    # Standard Monte Carlo: daily log returns drawn from a Normal(mean, variance)
    mean, var = P1.cal_stats(P1.cal_returns(data))
    simulated_returns = rng.normal(mean, var ** 0.5, size=(N_PATHS, N_DAYS))
    return build_paths(data.iloc[-1], simulated_returns)


def GBM_Simulator(data):
    # Geometric Brownian Motion: dS = mu*S*dt + sigma*S*dW, simulated through its log-return form
    # log-return per day = (mu - sigma^2/2)*dt + sigma*sqrt(dt)*Z,  Z ~ N(0,1)
    mean, var = P1.cal_stats(P1.cal_returns(data))
    dt = 1 / TRADING_DAYS
    sigma = (var * TRADING_DAYS) ** 0.5
    mu = mean * TRADING_DAYS + 0.5 * sigma ** 2

    Z = rng.standard_normal(size=(N_PATHS, N_DAYS))
    simulated_returns = (mu - 0.5 * sigma ** 2) * dt + sigma * dt ** 0.5 * Z
    return build_paths(data.iloc[-1], simulated_returns)


def Bootstrapping_Simulator(data):
    # Bootstrapping: daily log returns resampled (with replacement) from the empirical returns
    returns = P1.cal_returns(data).to_numpy()
    simulated_returns = rng.choice(returns, size=(N_PATHS, N_DAYS), replace=True)
    return build_paths(data.iloc[-1], simulated_returns)


MODELS = {
    "Geometric Brownian Motion": GBM_Simulator,
    "Standard Monte Carlo": Standard_Simulator,
    "Bootstrapping": Bootstrapping_Simulator,
}


# ------------------------------------------------------------------ Analysis
def Monte_Carlo_Simulations(data, model=Standard_Simulator):
    # Runs one model, plots it and prints the risk of loss
    simulated_paths = model(data)
    Plot_Monte_Carlo(simulated_paths)
    print(f"Estimated Risk of Loss: {Risk_Calculation(simulated_paths, data.iloc[-1]):.2f}%\n")


def Risk_Calculation(simulated_paths, P):
    # Calculating the risk of loss (final price < initial price), in %
    return np.mean(simulated_paths[:, -1] < P) * 100


def Comparison_of_Models(data):
    # Simulating paths using all three models and comparing their final price distributions
    simulated = {name: model(data) for name, model in MODELS.items()}
    starting_price = data.iloc[-1]

    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    fig.suptitle("Comparison of Models", fontsize=16, fontweight="bold")
    for ax, (name, paths) in zip(axes, simulated.items()):
        plot_histogram(ax, paths[:, -1], starting_price, name)
    plt.subplots_adjust(hspace=0.35, left=0.08, right=0.98, top=0.93, bottom=0.08)
    plt.show()

    # Comparing Risk of Loss
    for name, paths in simulated.items():
        print(f"Risk of Loss for {name}: {Risk_Calculation(paths, starting_price):.2f}%")
    print()


# ------------------------------------------------------------------ Plotting
def Plot_Monte_Carlo(simulated_paths):
    _, (a1, a2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plotting 100 simulated paths to visualize the price evolution
    a1.plot(simulated_paths[:100].T, color="gray", alpha=0.2)
    a1.set_title("Monte Carlo Simulation of Price Paths", fontweight="bold")
    a1.set_xlabel("Days", fontweight="bold")
    a1.set_ylabel("Price", fontweight="bold")
    a1.set_facecolor("lightgray")

    # Histogram of the final prices
    plot_histogram(a2, simulated_paths[:, -1], simulated_paths[0, 0])
    a2.set_title("Monte Carlo Histogram of Final Prices", fontweight="bold")

    plt.tight_layout()
    plt.show()


def plot_histogram(ax, final_prices, starting_price, model_name=None):
    # Histogram of final prices with the starting price and the most probable final price (mode)
    ax.hist(final_prices, bins=50, edgecolor="black", color="purple")
    ax.set_xlabel("Final Price" if model_name is None else f"Final Price :  {model_name}", fontweight="bold")
    ax.set_ylabel("Frequency", fontweight="bold")
    ax.set_facecolor("lightgray")

    counts, bins = np.histogram(final_prices, bins=50)
    i = np.argmax(counts)
    most_probable_price = (bins[i] + bins[i + 1]) / 2

    box = dict(facecolor="white", alpha=0.8, edgecolor="black")
    ax.text(0.985, 0.95, f"Starting Price: {starting_price:.2f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=10, bbox=box)
    ax.text(0.985, 0.83, f"Most Probable Final Price: {most_probable_price:.2f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=10, bbox=box)
