import streamlit as st 
import pandas as pd
import numpy as np
st.write("Hello World")

m = st.text_input("Favourite Movie")
# Concatenate
st.write(f"My favourite movie is:{m}")

# button 
is_clicked = st.button("Clicked")
st.write("### This is good")

#CSV Data 
data = pd.read_csv("movies.csv")
st.write(data)

st.write("### My Chart")

chart_data = pd.DataFrame(
    np.random.randn(10,3),
    columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)