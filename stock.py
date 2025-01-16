import streamlit as st
import pandas as pd
import yfinance as yf


st.write("# Stock Price App")

st.write("### Show the Closing Price and Volume of stock of Microsoft ")

ticker_symbol = "MSFT"

ticker_data = yf.Ticker(ticker_symbol)

tickerDf = ticker_data.history(period = '1d' ,start = "2010-1-1", end = "2020-1-25")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Open)







