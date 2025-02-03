import streamlit as st
import pandas as pd, numpy as np, matplotlib.pyplot as plt

def main() :
    # Read pandas DataFrame
    df = pd.read_csv('data/iris.csv')

    # Display the DataFrame on the web page
    st.title('Iris Data Analysis')
    st.dataframe(df)
    # Display the unique values of column 'species'
    st.subheader('Unique values of column \'species\'')
    st.dataframe(df['species'].unique())
    # Display the number of data on the web page
    st.info(f'Total number of the data is {df.shape[0]}.')
    


if __name__ == '__main__' :
    main()