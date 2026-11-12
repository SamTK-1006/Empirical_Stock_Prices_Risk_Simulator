import numpy as np
import plotly.graph_objects as go
import streamlit as st

import Phase_1_Empirical_Time_Series as P1

# Simulating paths for 756 trading days (3 years)
N_DAYS = 756


def Monte_Carlo_Simulations(data):
    # Renders the Monte Carlo Simulations page
    n_paths = st.slider("Number of Simulations:", min_value=100, max_value=5000, value=1000, step=100)

    P = float(data.iloc[-1])
    simulated_paths = simulator(data, n_paths)
    final_prices = simulated_paths[:, -1]

    c1, c2, c3 = st.columns(3)
    c1.metric("Starting Price", f"{P:,.2f}", border=True)
    c2.metric("Most Probable Final Price", f"{most_probable_price(final_prices):,.2f}", border=True)
    c3.metric("Risk of Loss", f"{Risk_Calculation(simulated_paths, P):.2f}%", border=True)

    paths_fig, hist_fig = Plot_Monte_Carlo(simulated_paths)
    st.plotly_chart(paths_fig, width="stretch")
    st.plotly_chart(hist_fig, width="stretch")


def simulator(data, n_paths):
    # Daily log returns drawn from a Normal(mean, variance) and compounded from the last price
    mean, var = P1.cal_stats(P1.cal_returns(data))
    simulated_returns = np.random.default_rng().normal(mean, var ** 0.5, size=(n_paths, N_DAYS))
    cumulative = np.hstack([np.zeros((n_paths, 1)), np.cumsum(simulated_returns, axis=1)])
    return data.iloc[-1] * np.exp(cumulative)


def most_probable_price(final_prices):
    # Midpoint of the most frequent histogram bin (the mode)
    counts, bins = np.histogram(final_prices, bins=50)
    i = np.argmax(counts)
    return (bins[i] + bins[i + 1]) / 2


def Risk_Calculation(simulated_paths, P):
    # Calculating the risk of loss (final price < initial price), in %
    return float(np.mean(simulated_paths[:, -1] < P) * 100)


def Plot_Monte_Carlo(simulated_paths):
    P = simulated_paths[0, 0]
    final_prices = simulated_paths[:, -1]

    # Plotting 10% of the simulated paths to visualize the price evolution (drawn as one NaN-separated trace)
    k = int(0.1 * len(simulated_paths))
    days = np.arange(simulated_paths.shape[1])
    xs = np.tile(np.append(days, np.nan), k)
    ys = np.hstack([simulated_paths[:k], np.full((k, 1), np.nan)]).ravel()

    paths_fig = go.Figure(go.Scatter(x=xs, y=ys, mode="lines", line=dict(color="rgba(120,120,120,0.35)", width=1),
                                     hoverinfo="skip"))
    paths_fig.add_hline(y=P, line=dict(color="red", dash="dash"), annotation_text="Start")
    paths_fig.update_layout(title="Monte Carlo Simulation of 10% of Price Paths", xaxis_title="Days",
                            yaxis_title="Price", showlegend=False)

    # Histogram of the final prices
    hist_fig = go.Figure(go.Histogram(x=final_prices, nbinsx=50,
                                      marker=dict(color="purple", line=dict(color="black", width=1))))
    hist_fig.add_vline(x=P, line=dict(color="red", dash="dash"), annotation_text="Start",
                       annotation_position="top left")
    hist_fig.add_vline(x=most_probable_price(final_prices), line=dict(color="green", dash="dot"),
                       annotation_text="Most probable", annotation_position="top right")
    hist_fig.update_layout(title="Histogram of Final Prices", xaxis_title="Final Price", yaxis_title="Frequency",
                           showlegend=False)

    return P1.style(paths_fig, 480), P1.style(hist_fig, 480)
