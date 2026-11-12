import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf
from plotly.subplots import make_subplots


# ---------------------------------------------------------------------- Data
@st.cache_data(ttl=3600, show_spinner="Fetching market data...")
def _download(ticker):
    # Downloads 3 years of daily closing prices as a Series (raises on bad data so failures are never cached)
    raw = yf.download(ticker, period="3y", interval="1d", auto_adjust=True, progress=False)
    data = raw["Close"].squeeze().dropna() if not raw.empty else None
    if not isinstance(data, pd.Series) or len(data) < 30:
        raise ValueError(f"No usable data for '{ticker}'")
    return data


def load_data(ticker):
    # Returns the closing prices for a ticker, or None if it is invalid
    try:
        return _download(ticker)
    except Exception:
        return None


def require_data():
    # Used by every page: returns the loaded data, or stops the page with a friendly message
    data = st.session_state.get("data")
    if data is None:
        st.info("Enter a valid ticker symbol in the sidebar to get started.", icon="👈")
        st.stop()
    return data


# ------------------------------------------------------------------ Analysis
def cal_returns(data):
    # Calculates the (log) Returns
    return np.log(data / data.shift(1)).dropna()


def cal_stats(returns):
    # Calculates the Mean and Variance of the Returns
    return float(returns.mean()), float(returns.var())


def use_yahoo(data):
    # Renders the Time Series Analysis page
    mean, var = cal_stats(cal_returns(data))

    c1, c2, c3 = st.columns(3)
    c1.metric("Mean Return", f"{mean:.6f}", border=True)
    c2.metric("Return Std Dev", f"{np.sqrt(var):.6f}", border=True)
    c3.metric("Return Variance", f"{var:.6f}", border=True)

    st.plotly_chart(data_plot(data), width="stretch")


# ------------------------------------------------------------------ Plotting
def style(fig, height):
    # Shared look for every chart
    fig.update_layout(height=height, margin=dict(l=10, r=10, t=60, b=10))
    if fig.layout.title.text:  # a font size on an empty title makes Plotly print "undefined"
        fig.update_layout(title_font_size=18)
    fig.update_xaxes(gridcolor="rgba(128,128,128,0.2)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(128,128,128,0.2)", zeroline=False)
    return fig


def data_plot(data):
    # Plots the Price and Returns
    fig = make_subplots(rows=2, cols=1, vertical_spacing=0.16, subplot_titles=("Close Price", "Returns"))

    fig.add_scatter(x=data.index, y=data.to_numpy(), mode="lines", line=dict(color="blue", width=2),
                    hovertemplate="%{x|%d %b %Y}<br>Price: %{y:,.2f}<extra></extra>", row=1, col=1)
    fig.add_histogram(x=cal_returns(data), nbinsx=20, marker=dict(color="orange", line=dict(color="black", width=1)),
                      row=2, col=1)

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_xaxes(title_text="Return Values", row=2, col=1)
    fig.update_yaxes(title_text="Frequency", row=2, col=1)
    fig.update_layout(showlegend=False)
    return style(fig, 650)
