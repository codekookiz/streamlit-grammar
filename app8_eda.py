"""
# File that processes when the user chooses 'EDA'
"""


import streamlit as st, pandas as pd, matplotlib.pyplot as plt


def run_eda() :
    st.subheader('Exploratory Data Analysis')
    st.text('We\'re analyzing the data of Iris.')
    # Read 'iris.csv' file
    df = pd.read_csv('data/iris.csv')
    # Display the columns that user has chosen
    selected_columns = st.multiselect('Choose which columns to display :', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe(df[selected_columns])
        # Display the Correlation Coefficient of the chosen columns
        st.text('Correlation Coefficient is :')
        st.dataframe(df[selected_columns].corr(numeric_only = True))
    