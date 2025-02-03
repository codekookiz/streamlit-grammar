import streamlit as st, pandas as pd

def main() :
    df = pd.read_csv('data/iris.csv')

    # If user presses the 'Show data' button, the dataframe will be displayed on the web page 
    if st.button('Show data') :
        st.dataframe(df)

    # If user presses the 'Upper case' button, the values of column 'species' will be displayed on the web page
    if st.button('Upper case') :
        st.dataframe(df['species'].str.upper())

    # Radio button : the user can choose one of the options
    st.radio('Select the color :', ['Red', 'Yellow', 'Blue'])

    # Radio button : the user can choose two of the sort methods
    my_choice = st.radio('Choose the sort option of column \'petal_length\' :', ['Ascending', 'Descending'])
    if my_choice == 'Ascending' :
        st.dataframe(df.sort_values('petal_length'))
    else :
        st.dataframe(df.sort_values('petal_length', ascending = False))


if __name__ == '__main__' :
    main()