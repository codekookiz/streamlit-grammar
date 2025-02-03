"""
# File that processes when the user chooses 'Home'
"""


import streamlit as st


def run_home() :
    st.subheader('Home Page')
    st.text('This App is for Streamlit practice.')
    st.image('data/image_03.jpg', width = 300)