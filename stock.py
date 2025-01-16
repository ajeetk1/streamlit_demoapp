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

# Pandas Data Frame
tickerDf = ticker_data.history(period = '1d' ,start = "2010-1-1", end = "2020-1-25")

st.write("## Close Stock Price")
st.line_chart(tickerDf.Close)

st.write ("## Volume of Stock")
st.line_chart(tickerDf.Volume)

st.write("## Open Stock Price")
st.line_chart(tickerDf.Open)







