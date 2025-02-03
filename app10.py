"""
# Charts from the Web Environment (Methods from Streamlit)
"""


import streamlit as st, plotly.express as px, pandas as pd


def main() :
    df = pd.read_csv('data/lang_data.csv')

    st.subheader('Popularity of Programming Languages')
    selected_columns = st.multiselect('Choose Languages :', df.columns)
    if len(selected_columns) != 0 :
        df_selected = df[selected_columns]
        
        # Line Chart from Streamlit
        st.line_chart(df_selected)

        # Area Chart from Streamlit
        st.area_chart(df_selected)

    df2 = pd.read_csv('data/location.csv', index_col = 0)
    st.dataframe(df2)

    # Map Chart from Streamlit
    st.map(df2)

    df3 = pd.read_csv('data/prog_languages_data.csv', index_col = 0)
    st.dataframe(df3)

    # Pie Chart from Plotly Express
    fig1 = px.pie(data_frame = df3, names = 'lang', values = 'Sum')
    st.plotly_chart(fig1)
    fig2 = px.pie(data_frame = df3.loc['R':'Python', :], names = 'lang', values = 'Sum')
    st.plotly_chart(fig2)

    # Bar Chart from Plotly Express
    df3.sort_values('Sum', ascending = False, inplace = True)
    fig3 = px.bar(data_frame = df3, x = 'lang', y = 'Sum')
    st.plotly_chart(fig3)


if __name__ == '__main__' :
    main()