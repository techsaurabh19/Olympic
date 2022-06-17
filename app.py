import streamlit as st
import pandas as pd

import helper
import preprocessor

df = preprocessor.preprocess()
user_menu = st.sidebar.radio(
    'select an Option',
    ("Medal Tally", 'Overall Analysis', 'Country-Wise Analysis', 'Athlete wise Analysis')
)

st.dataframe(df)

if user_menu=='Medal Tally':
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)