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

#Web scrappping of NBA player stats
def load_data(year):
    url=  "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

#Sidebar - Position Selection
sorted_unique_team =sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team)

#Sidebar - Position Selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos)
