import streamlit as st
import pandas as pd

st.title("Data Exploration")

st.header('Uploading data')
data_file = st.file_uploader("Choose a file")

st.header('Visualizing data')
if data_file is not None:
  df = pd.read_csv(data_file)
  st.dataframe(df)

st.header('Descriptive Statistics')
st.table(df.describe())
