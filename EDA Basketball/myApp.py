import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer')

st.markdown("""
    This app performs simple webscrapping of NBA player stats Data!
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',list(reversed(range(1950,2020))))
