# Load Modules 
import pandas as pd
import numpy as np 
import streamlit as st


#Title

st.title("Streamlit App for Walmart Cash Application")

## Ingest Data 

### Create a file uploader for remittance file in your Streamlit app ####
remittance_file = st.file_uploader("Select Walmart Remittance Detail. Choose a CSV file", type='csv', accept_multiple_files=False)

### Create a file uploader for DG detail file in your Streamlit app ####
detail_file = st.file_uploader("Select Corresponding Details Report. Choose a CSV File", type ='csv', accept_multiple_files=False)

### Store remittance detail file

remit = pd.read_csv(remittance_file)

### Store Details Report 

detail = pd.read_csv(detail_file)

## Merge()  VLOOKUP Equivalent

### Change data type to string
remit['poMatch']  = remit['Invoice Number'].astype('string')
detail['poMatch']  = detail['Purchase Order Number'].astype('string')

### Clean up string to remove '.0'
remit['poMatch'] = remit['poMatch'].str.replace(r'\.0$', '', regex=True)

### Save new data frames to be merged 
remit_review = remit[['poMatch','Amount Paid($)','Invoice Date','Store Number','DEDUCTION CODE']]
detail_review = detail[['Invoice Number','poMatch','Ship-To Customer Name']]


mergeFile = remit_review.merge(detail_review, on='poMatch', how ='left')

### Remove duplicates 
mergeFile_cleaned = mergeFile.drop_duplicates()

#Needs Review Function
def needs_review(df):
    # Fill empty Invoice Number values with "Needs Review"
    df['Invoice Number'] = df['Invoice Number'].fillna("Needs Review")
    return df  

#Define DC Location Function

dc = 8011

def dc_location(df):
    df.loc[df['Store Number'] == dc, 'Invoice Number'] = df['poMatch'].str.replace(r'\.0$', '', regex=True)
    return df

## Download Data 
st.title("Merged Data Load")

mergeFile_cleaned = needs_review(mergeFile_cleaned)
dc_defined = dc_location(mergeFile_cleaned)

if dc_defined is not None:
    st.write(dc_defined)