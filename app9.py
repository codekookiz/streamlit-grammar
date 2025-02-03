"""
# Charts from Jupyter Notebook
"""


import streamlit as st, pandas as pd, matplotlib.pyplot as plt, seaborn as sb, matplotlib.font_manager as fm

# Allow to use Korean in Streamlit Chart
font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
font_name = fm.FontProperties(fname = font_path).get_name()
plt.rc('font', family = font_name)

def main() :
    st.title('Draw Charts')
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

    st.subheader('Scatterplot')
    fig1 = plt.figure() # Define where the Chart will be shown
    plt.scatter(data = df, x = 'petal_length', y = 'petal_width')
    # plt.show() : How it is done in Jupyter Notebook
    plt.title('Ratio between petal_length and petal_width')
    plt.xlabel('petal_length')
    plt.ylabel('petal_width')
    st.pyplot(fig1)

    fig2 = plt.figure()
    sb.regplot(data = df, x = 'petal_length', y = 'petal_width')
    st.pyplot(fig2)

    st.text('Histogram')
    fig3 = plt.figure()
    plt.hist(data = df, x = 'petal_length', rwidth = 0.8)
    st.pyplot(fig3)

    fig4 = plt.figure()
    plt.hist(data = df, x = 'petal_length', rwidth = 0.8, bins = 20)
    st.pyplot(fig4)
    
    fig5 = plt.figure()
    plt.subplot(1, 2, 1)
    plt.hist(data = df, x = 'petal_length', rwidth = 0.8)
    plt.subplot(1, 2, 2)
    plt.hist(data = df, x = 'petal_length', rwidth = 0.8, bins = 20)
    st.pyplot(fig5)

    # Display dataframe from pandas into Chart : how many data are in column 'species'
    fig6 = plt.figure()
    sb.countplot(data = df, x = 'species')
    st.pyplot(fig6)

    fig7 = plt.figure()
    df['species'].value_counts().plot(kind = 'bar')
    plt.xticks(rotation = 0)
    st.pyplot(fig7)

    fig8 = plt.figure()
    sb.heatmap(data = df.corr(numeric_only = True), cmap = 'coolwarm', annot = True, vmin = -1, vmax = 1)
    st.pyplot(fig8)




if __name__ == '__main__' :
    main()