"""
# Charts from the Web Environment (Methods from Streamlit)
"""


import streamlit as st, plotly.express as px, pandas as pd


def main() :
    df = pd.read_csv('data/lang_data.csv')
    st.dataframe(df)


if __name__ == '__main__' :
    main()