import streamlit as st
import Phase_3_Monte_Carlo

# Setting up the Streamlit title
st.title("Monte Carlo Simulation")

# Introduction to Monte Carlo Simulation
st.markdown("""
Monte Carlo simulation is used to model multiple possible future stock price paths
based on the historical behavior of the asset.

Rather than predicting a single future price, the simulation generates many
possible outcomes by introducing randomness into the price evolution process.

The slider allows the number of simulations to be adjusted dynamically,
typically ranging from 100 to 5000 simulations.

A higher number of simulations generally produces a smoother and more stable
distribution of outcomes, while a smaller number provides a quicker but less
detailed approximation.
""")
st.divider()

# Visualization of Simulations
st.subheader("Visualization of Simulations")
data = st.session_state.get("data")
if data is not None:
        Phase_3_Monte_Carlo.Monte_Carlo_Simulations(data)

else:
    st.write("Please enter a ticker symbol in the main page to view the Monte Carlo simulations.")

st.divider()

# Explanation of the Simulations
st.subheader("Simulated Price Paths")
st.markdown("""
Each line in the simulation plot represents one possible future trajectory
of the stock price under the assumptions of the model.

Because random returns are generated during each simulation, every path evolves
differently but still centred around the same mean and standard deviation, reflecting the uncertainty and variability present in financial markets.

By observing the density of many simulated trajectories together, it becomes possible to visualize:
- potential future price ranges
- uncertainty in market behavior
- volatility over time
- optimistic and pessimistic scenarios

The spread between the paths increases over time, illustrating how uncertainty
accumulates as the forecasting horizon becomes longer.
            
In the above plot, only 10% of the simulated paths are shown to maintain clarity and avoid overcrowding, while still providing a representative visualization of the range of possible future price evolutions.
A slider has been provided to adjust the number of simulations, allowing users to explore how the density and spread of the simulated paths change with different numbers of simulations, with accuracy of risk of loss increasing
with the increase in the number of simulations.
""")

st.divider()

# Explanation of the Distribution of Final Prices
st.subheader("Distribution of Final Prices")
st.markdown("""
The histogram of final simulated closing prices summarizes the outcomes
at the end of the simulation horizon.

Each bar represents the frequency of simulated closing prices falling within
a particular range.

This distribution provides insight into:

- the most likely future closing price range
- the spread of possible outcomes
- the probability of extreme price movements
- overall uncertainty in the forecast

The peak of the histogram corresponds to the region where simulated outcomes
occur most frequently.

Although the simulation is based on historical statistics and simplifying assumptions,
it provides a useful probabilistic framework for understanding potential future behavior
rather than a precise prediction of future prices.
""")

st.divider()

# Explanation of the Risk of Loss
st.subheader("Risk of Loss")
st.markdown("""
The risk of loss is calculated as the proportion of simulated paths that end with a final price below the initial price.
This metric quantifies the probability of experiencing a loss over the simulation horizon based on the historical return characteristics of the stock. 
            
However, it is important to remember that the Monte Carlo simulation relies on assumptions such as normally distributed returns and constant volatility, which may not fully capture the complexities of real market behavior. 
As mentioned before, adding more factors such as volume, and indicators can help to create a more realistic and reliable model.

Therefore, while the risk of loss provides a useful estimate based on the model, it should be interpreted with caution and supplemented with other forms of analysis when making investment decisions.
""")