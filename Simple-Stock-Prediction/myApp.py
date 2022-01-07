import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price Appp

Shown are the stock **closing price** and ***volume*** of Google
""")

#Defines ticker symbol
tickerSymbol = 'GOOGL'
#get data  on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for the ticker

tickerDf = tickerData.history(period='1d', start='2010-1-1',end='2022-1-1')
#Open High LOw CLose Volume Dividends Stock splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)