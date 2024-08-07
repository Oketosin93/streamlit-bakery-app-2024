import streamlit as st 
import numpy as np 
import pandas as pd 


def load_data():
    file = 'bakerysales.csv'
    df = pd.read_csv(file)
    df.unit_price = df.unit_price.str.replace(',','.').str.replace('€', '').str.strip()
    df.unit_price = df.unit_price.astype('float')
    return df.head(100)

#load the dataset
df = load_data()

# display the table
st.dataframe(df)