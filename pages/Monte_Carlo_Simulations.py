import streamlit as st

import Phase_1_Empirical_Time_Series as P1
import Phase_3_Monte_Carlo as P3

st.title("🎲 Monte Carlo Simulations")
P3.Monte_Carlo_Simulations(P1.require_data())
