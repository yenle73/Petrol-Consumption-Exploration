import streamlit as st
import pandas as pd
import io

st.title("Data Exploration")

st.header('Uploading data')
data_file = st.file_uploader("Choose a file", type=(['.csv']))

st.header('Visualizing data')
if data_file is not None:
  df = pd.read_csv(data_file)
  st.dataframe(df)
  
  st.header('Descriptive Statistics')
  st.table(df.describe())

  st.header('Data Information')
  buffer = io.StringIO
  df.info(buf=buffer)
  st.write(buffer.getvalue())
