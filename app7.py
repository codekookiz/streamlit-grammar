"""
# Uploading files & Sidebar
"""


import streamlit as st, pandas as pd
from datetime import datetime


def save_uploaded_file(directory, file) :
    import os
    if not os.path.exists(directory) :
        os.makedirs(directory)
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    st.success(f'Succeeded to save, Path : {directory}/{file.name}')


def main() :
    st.title('Example : File Upload')
    st.sidebar.title('Sidebar')
    menu = ['Image File', 'CSV File', 'PDF File']
    choice = st.sidebar.selectbox('What to upload :', menu)
    print(choice)

    if choice == menu[0] :
        # Step 1 : Upload the image file
        file = st.file_uploader('Upload Image File :', type = ['jpg', 'png', 'jpeg', 'webp'])
        # Step 2 : Make the file name Unique
        if file is not None :
            new_filename = datetime.now().isoformat().replace(':', '_') + '.jpg'
            file.name = new_filename
            # Step 3 : Save image file
            save_uploaded_file('images', file)
            # Step 4 : Show saved image on webpage
            st.image(file, use_container_width = True)

    elif choice == menu[1] :
        file = st.file_uploader('Upload CSV File', type = ['csv'])
        if file is not None :
            # Step 1 : Upload the csv file
            save_uploaded_file('csv', file)
            # Step 2 : Read csv file and display it on webpage
            df = pd.read_csv(file)
            st.dataframe(df)

    else :
        file = st.file_uploader('Upload PDF File', type = ['pdf'])
        if file is not None :
            # Step 1 : Upload the pdf file
            save_uploaded_file('pdf', file)
            # Step 2 : Display pdf file on webpage
            st.write(file) # Cuz the library for PDF reader isn't imported right now, we cannot display this as form of PDF


if __name__ == '__main__' :
    main()