import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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
  buffer = io.StringIO()
  df.info(buf=buffer)
  st.text(buffer.getvalue())

  st.header('Visualize each attribute')
  for col in list(df.columns):
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=20)
    plt.xlabel(col)
    plt.ylabel('Quanity')
    st.pyplot(fig)

  st.header('Covariance')
  correlation_matrix = np.corrcoef(df, rowvar=False)
  fig, ax = plt.subplots()
  sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
  st.pyplot(fig)
