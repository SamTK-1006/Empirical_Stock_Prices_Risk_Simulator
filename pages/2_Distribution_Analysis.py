import streamlit as st
import Phase_2_Distribution

# Setting up the Streamlit title
st.title("Distribution Analysis")

# Introduction to Distribution Analysis
st.markdown("""
Financial returns are often modeled using probability distributions in order to study risk, volatility, and future price behavior.

This section analyzes the distribution of daily returns using:

- A histogram of returns
- A normal distribution overlay
- A Q-Q (Quantile-Quantile) plot""")

st.divider()
data = st.session_state.get("data")

# Distribution Analysis
st.subheader("Distribution of Returns")
if data is not None:
    Phase_2_Distribution.distribution_ticker(data)   
else:
    st.write("Please enter a ticker symbol in the main page to view the Distribution of Returns.")

# Explanation of the Returns Histogram with Normal Distribution Overlay
with st.expander("Returns Histogram with Normal Distribution Overlay"):
    st.markdown("""The histogram shows the empirical distribution of returns observed in the market data.
                
A normal distribution curve is overlaid using the sample mean and standard deviation of the returns.
                
This allows us to compare:
- the theoretical normal distribution, and
- the actual observed market behavior.
                
Although the distribution may appear approximately bell-shaped, real financial returns often exhibit:
- heavier tails (corners),
- skewness (asymmetry),
- and extreme movements more frequently than predicted by a perfect normal distribution.

These extreme events are especially visible during periods of high market volatility.""")
    
with st.expander("Why Use the Normal Distribution?"):
    st.markdown("""
The real market usually has extreme events that are not captured by the normal distribution. However, despite its limitations, it remains one of the most widely used assumptions in quantitative finance because it provides:
- mathematical simplicity,
- computational efficiency,
- and a strong baseline model for statistical analysis.

Many foundational models in finance, including Monte Carlo simulations and risk modeling begin with the assumption of normally distributed returns.

Therefore, even though empirical returns are not perfectly normal, the normal approximation is still useful for:
- understanding general market behavior,
- estimating volatility,
- and generating simulated future price paths.

The goal is not to claim that markets are perfectly normal, but rather to use the normal distribution as a practical and interpretable modeling framework.
                """)

with st.expander("Formula for Normal Distribution Overlay"):
    st.markdown("""
The normal distribution overlay is generated using the probability density function:
""")

    st.latex(r"f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}")

    st.markdown(r"""
where:
- $\mu$ = mean of returns  
- $\sigma$ = standard deviation of returns  
- $x$ = return value  

The mean and standard deviation are estimated from the historical return data.
This normal distribution is then overlaid on the returns histogram
to compare the theoretical distribution with the empirical market data.
""")

st.divider()

# Explanation of the Q-Q Plot
st.subheader("Q-Q Plot")
if data is not None:
    Phase_2_Distribution.generate_qq(data)
else:
    st.write("Please enter a ticker symbol in the main page to view the Q-Q plot.")
    
with st.expander("Q-Q Plot"):
    st.markdown("""
The Q-Q plot compares the quantiles of the real returns against the quantiles of a theoretical normal distribution.

If the returns were perfectly normally distributed, the points would lie approximately along the straight diagonal red line. Deviations from this line, particularly in the tails, indicate departures from normality and highlight the presence of extreme market events.

In financial datasets, it is common to observe tail deviations, reflecting the fact that large gains and losses occur more frequently than predicted by the normal distribution.
                
This brings us to the conclusion that although the there are deviations from normality at the ends, we can still use normal deviation to model the general behaviour of the stock returns, keeping in mind to add in more factors to account for the extreme events. Adding in more facts helps increase the accuracy of the simulations.
                """)

with st.expander("Formula for Q-Q Plot"):
    st.markdown("""
The Q-Q plot is constructed by comparing the ordered sample quantiles
with the theoretical quantiles from a normal distribution.
""")

    st.latex(r"Q_{\mathrm{empirical}} = \mathrm{sort}(R_t)")

    st.latex(r"Q_{\mathrm{theoretical}} = \Phi^{-1}\left(\frac{i-0.5}{n}\right)")

    st.markdown(r"""
where:
- $R_t$ = returns  
- $\Phi^{-1}$ = inverse CDF (quantile function) of the normal distribution  
- $i$ = rank of the observation  
- $n$ = total number of observations  
                
The empirical quantiles are obtained by sorting the returns, while the theoretical quantiles are calculated using the 
inverse CDF of the normal distribution based on the rank of each observation. 
The resulting plot allows us to visually assess how well the empirical data matches the theoretical normal distribution.
""")
    
# Conclusion of the Distribution Analysis
st.markdown("""
We will further assume normality in the Monte Carlo simulations, which is explored in the next section.
""")