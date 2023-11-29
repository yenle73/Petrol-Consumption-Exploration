import streamlit as st
import pandas as pd

st.title("Data Exploration")

st.header('Uploading data')
uploaded_file = st.file_uploader("Choose a file")

st.header('Visualizing data')
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)
