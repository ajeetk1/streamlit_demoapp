import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

image = Image.open("logo-dna.jpg")

st.image(image,use_container_width =True) 

st.write("#DNA Nucleotide Count Web App")

st.write("### This app counts the nucleotide of query DNA!")

### Input Text Box 

st.header("Enter DNA sequence")

#st.write("#### Sequence Input")
#st.text_input()

# DNA Input
sequence_input = ">DNA Query 2 \n GADADADCCCCCCSFFFFFFEERDDVDDDDDFFDFVFVFFEREREFREFREFREFRTHYJHNFCSDCDSCDFFBGBDCSCFVDFCD"

# Input Box or Text Box

sequence = st.text_area("Sequence input",sequence_input, height=200)

sequence = sequence.splitlines()

sequence = sequence[1:] 
sequence
sequence = "".join(sequence)

st.write("### ***" )

# INPUT PRINT

st.header('INPUT (DNA Query)')
sequence

## DNA Nucleatide Count
st.header('OUTPUT (DNA Nucleotide Count)')

