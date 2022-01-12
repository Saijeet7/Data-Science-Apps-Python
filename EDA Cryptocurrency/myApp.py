import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

#Page layout
##Page expands to full width
st.set_page_config(layout="wide")
st.title('Crypto Price App')
st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrency
""")

#About
expander_bar = st.expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:** [CoinMarketCap](http://coinmarketcap.com).
* **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf).
""")

col1=st.sidebar
col2,col3 = st.columns((2,1))

#Sidebar + main panel
col1.header('Input Options')

##Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Select currency for price',('USD','BTC','ETH'))


