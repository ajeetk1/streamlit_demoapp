import streamlit as st
import pandas as pd
import yfinance as yf

# MarkDown Heading 
st.write("# Stock Price App")

# SubHeading we are taking Closing,volume and Open Prices 
st.write("### Show the Closing Price and Volume of stock of Microsoft ")


# Taking Ticker Symbol
ticker_symbol = "MSFT"

# Data for Ticker Symbol
ticker_data = yf.Ticker(ticker_symbol)

tickerDf = ticker_data.history(period = '1d' ,start = "2010-1-1", end = "2020-1-25")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Open)







