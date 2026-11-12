import numpy as np
import plotly.graph_objects as go
import scipy.stats as sc
import streamlit as st

import Phase_1_Empirical_Time_Series as P1


def distribution_analysis(data):
    # Renders the Distribution Analysis page
    tab1, tab2 = st.tabs(["Normal Distribution Overlay", "Q-Q Plot"])
    tab1.plotly_chart(distribution_ticker(data), width="stretch")
    tab2.plotly_chart(generate_qq(data), width="stretch")


def distribution_ticker(data):
    # Comparing distribution of returns with normal distribution
    returns = P1.cal_returns(data)
    mean, var = P1.cal_stats(returns)

    fig = go.Figure()
    fig.add_histogram(x=returns, nbinsx=20, histnorm="probability density", name="Returns",
                      marker=dict(color="orange", line=dict(color="black", width=1)))

    # Plotting normal distribution overlay
    pad = 0.1 * (returns.max() - returns.min())
    x = np.linspace(returns.min() - pad, returns.max() + pad, 1000)
    fig.add_scatter(x=x, y=sc.norm.pdf(x, mean, var ** 0.5), mode="lines", name="Normal Distribution",
                    line=dict(color="black", width=2))

    fig.update_layout(title="Normal Distribution Overlay", xaxis_title="Return Values", yaxis_title="Density",
                      legend=dict(orientation="h", y=1.1, x=1, xanchor="right"))
    return P1.style(fig, 520)


def generate_qq(data):
    # Q-Q plot to compare empirical returns with theoretical normal distribution
    returns = P1.cal_returns(data)
    mean, var = P1.cal_stats(returns)
    returns = np.sort(returns.to_numpy())
    n = len(returns)

    # Generating theoretical quantiles
    theoretical = sc.norm.ppf(np.linspace(1 / n, (n - 1) / n, n), loc=mean, scale=var ** 0.5)
    lo, hi = min(theoretical.min(), returns.min()), max(theoretical.max(), returns.max())

    fig = go.Figure()
    fig.add_scatter(x=theoretical, y=returns, mode="markers", name="Returns", marker=dict(color="blue", size=6))
    fig.add_scatter(x=[lo, hi], y=[lo, hi], mode="lines", name="Normal", line=dict(color="red", dash="dash"))

    # Equal axis scaling so the plot is square and properly scaled
    fig.update_layout(title="Q-Q Plot", xaxis_title="Theoretical Quantiles", yaxis_title="Empirical Quantiles",
                      legend=dict(orientation="h", y=1.1, x=1, xanchor="right"),
                      xaxis=dict(range=[lo, hi]), yaxis=dict(range=[lo, hi], scaleanchor="x", scaleratio=1))
    return P1.style(fig, 600)
