import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

# Adding the Logo Image
image = Image.open("logo-dna.jpg")

# Setting the image as the container width
st.image(image,use_container_width =True) 

st.write("#DNA Nucleotide Count Web App")

st.write("### This app counts the nucleotide of query DNA!")

### Input Text Box 

st.header("Enter DNA sequence")

#st.write("#### Sequence Input")
#st.text_input()

# DNA Input
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# Input Box or Text Box

sequence = st.text_area("Sequence input",sequence_input, height=200)
# Split the entire DNA sequence in multi-lines
sequence = sequence.splitlines()

# Not counting the first line and count from the second line
sequence = sequence[1:] 
sequence
# Concatenates the complete DNA sequence
sequence = "".join(sequence) 

st.markdown("---") #Horizonal Line

# INPUT PRINT

st.header('INPUT (DNA Query)')
sequence

## DNA Nucleatide Count
st.header('OUTPUT (DNA Nucleotide Count)')

# To Count the Characters in DNA Sequence use Dictionary Function 
# Empty Dictionary
st.subheader('1. Print Dictionary')
# Dictionary Python
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)
X

st.markdown("---") # Horizontal Line

### 3. Display DataFrame
st.subheader('2. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)