# Load Modules 
import pandas as pd
import numpy as np 
import streamlit as st

#Title

st.title("Streamlit App for Walmart Cash Application")

# Ingest Data 

####Create a file uploader in your Streamlit app
uploaded_files = st.file_uploader("Choose a CVS file", type='cvs', accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write("Filename: ", uploaded_file.name)
