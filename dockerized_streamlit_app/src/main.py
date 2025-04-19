import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Home page
st.title('Streamlit Dockerized App')
st.write("Welcome to the Dockerized Streamlit app!")

# Data Explorer
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Visualization
    fig = plt.figure(figsize=(10, 6))
    plt.plot(df.index, df.iloc[:, 0], label=df.columns[0])
    plt.title('Sample Plot')
    plt.xlabel('Index')
    plt.ylabel(df.columns[0])
    plt.legend()
    st.pyplot(fig)
