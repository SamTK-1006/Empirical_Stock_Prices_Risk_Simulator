import streamlit as st

import Phase_1_Empirical_Time_Series as P1

st.title("📈 Time Series Analysis")
P1.use_yahoo(P1.require_data())
