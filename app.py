# Load Modules 
import pandas as pd
import numpy as np 
import streamlit as st

#Title

st.title("Streamlit App for Walmart Cash Application")

# Ingest Data 

#### Create a file uploader for remittance file in your Streamlit app ####
remittance_files = st.file_uploader("Select Walmart Remittance Detail. Choose a CSV file", type='csv', accept_multiple_files=False)

#### Create a file uploader for DG detail file in your Streamlit app ####
detail_file = st.file_uploader("Select Corresponding Details Report. Choose a CSV File", type ='csv', accept_multiple_files=False)

#### Display remittance detail file

st.title("Remittance Detail")
remit = pd.read_csv(remittance_files)
st.write(remit)
