# Load Modules 
import pandas as pd
import numpy as np 
import streamlit as st


#Title

st.title("Streamlit App for Walmart Cash Application")

# Ingest Data 

#### Create a file uploader for remittance file in your Streamlit app ####
remittance_file = st.file_uploader("Select Walmart Remittance Detail. Choose a CSV file", type='csv', accept_multiple_files=False)

#### Create a file uploader for DG detail file in your Streamlit app ####
detail_file = st.file_uploader("Select Corresponding Details Report. Choose a CSV File", type ='csv', accept_multiple_files=False)

#### Store remittance detail file

st.title("Remittance Detail")
remit = pd.read_csv(remittance_file)

#### Store Details Report 
st.title("Details Report")
detail = pd.read_csv(detail_file)

# Combine into New Detail Frame

#### Merge()  VLOOKUP Equivalent

remit['poMatch']  = remit['Invoice Number'].astype('string')
detail['poMatch']  = detail['Purchase Order Number'].astype('string')
remit['poMatch'] = remit['poMatch'].str.replace(r'\.0$', '', regex=True)
remit_review = remit[['poMatch','Amount Paid($)']]
detail_review = detail[['Invoice Number','poMatch']]

#dataload = detail_review.merge(remit_review, on='poMatch', how ='right')
#st.write(dataload)
st.write(remit_review.shape)
st.write(detail_review.shape)