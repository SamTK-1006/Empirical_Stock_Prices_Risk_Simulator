import streamlit as st

import Phase_1_Empirical_Time_Series as P1
import Phase_2_Distribution as P2

st.title("📊 Distribution Analysis")
P2.distribution_analysis(P1.require_data())
