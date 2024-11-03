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

remit['poMatch']  = remit['Invoice Number']
detail['poMatch']  = detail['Purchase Order Number']
remit_review = remit[['poMatch','Amount Paid($)','Store Number','Invoice Date']]
detail_review = detail[['poMatch','Ship-To Customer Name','Invoice Number','Requested Delivery Date']]

dataload = pd.merge(remit_review,detail_review, on='poMatch', how ='left')

st.write(dataload)