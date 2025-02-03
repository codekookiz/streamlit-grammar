"""
# Development with File Division
"""


import streamlit as st
from app8_home import run_home
from app8_eda import run_eda
from app8_ml import run_ml
from app8_about_us import run_about_us


def main() :
    st.title('Example : Dashboard App')
    
    st.sidebar.title('Sidebar')
    menu = ['Home', 'EDA', 'ML', 'About Us'] # EDA : Exploratory Data Analysis, ML : Machine Learning
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()
    elif choice == menu[3] :
        run_about_us()


if __name__ == '__main__' :
    main()