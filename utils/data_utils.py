import pandas as pd
import streamlit as st

def load_data(file):
    data = pd.read_csv(file, header=None)
    column_names = [f'column_{i+1}' for i in range(data.shape[1])]
    data.columns = column_names
    return data

def display_data(data, title=""):
    if title:
        st.write(title)
    st.dataframe(data)