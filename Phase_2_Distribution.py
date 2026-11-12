import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

import Phase_1_Empirical_Time_Series as P1


def distribution_ticker(data):
    # Comparing distribution of returns with normal distribution
    returns = P1.cal_returns(data)
    mean, var = P1.cal_stats(returns)

    # Plotting the original histogram of returns
    _, ax = plt.subplots(figsize=(10, 6))
    ax.hist(returns, color="orange", edgecolor="black", bins=20, density=True)
    ax.set_title("Normal Distribution Overlay", fontweight="bold")
    ax.set_xlabel("Return Values", fontweight="bold")
    ax.set_ylabel("Density", fontweight="bold")
    ax.set_facecolor("lightgray")

    # Plotting normal distribution overlay
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 10000)
    ax.plot(x, sc.norm.pdf(x, mean, var ** 0.5), "black", linewidth=1.5)

    plt.tight_layout()
    plt.show()


def generate_qq(data):
    # Q-Q plot to compare empirical returns with theoretical normal distribution
    returns = P1.cal_returns(data)
    mean, var = P1.cal_stats(returns)
    returns = np.sort(returns.to_numpy())
    n = len(returns)

    # Generating theoretical quantiles
    theoretical = sc.norm.ppf(np.linspace(1 / n, (n - 1) / n, n), loc=mean, scale=var ** 0.5)

    plt.figure(figsize=(10, 6))
    plt.plot(theoretical, returns, color="blue", marker="o", linestyle="None")
    plt.plot(theoretical, theoretical, color="red", linestyle="--")

    # Setting limits to ensure the plot is square and properly scaled
    min_val = min(theoretical.min(), returns.min())
    max_val = max(theoretical.max(), returns.max())
    plt.xlim(min_val, max_val)
    plt.ylim(min_val, max_val)

    # Adding labels and title
    plt.xlabel("Theoretical Quantiles", fontweight="bold")
    plt.ylabel("Empirical Quantiles", fontweight="bold")
    plt.title("Q-Q Plot", fontweight="bold")

    plt.tight_layout()
    plt.show()
