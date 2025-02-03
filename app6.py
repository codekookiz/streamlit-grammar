"""
# Uploading image file
"""

import streamlit as st
from datetime import datetime


# A method to save uploaded file
def save_uploaded_file(directory, file) :
    # Step 1 : If the directory doesn't exist, create it
    import os
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # Step 2 : Save the file into the directory
    with open(os.path.join(directory, file.name), 'wb') as f: # 'w' means 'Write'
        f.write(file.getbuffer())
    # Step 3 : If it succeeded, display the success message on webpage
    st.success(f'Succeeded to save, Path : {directory}/{file.name}')


def main() :
    file = st.file_uploader('Choose the image file :', type = ['jpg', 'png', 'jpeg', 'webp']) # type : limit the extension of uploaded file
    if file is not None :
        # Only save the file when it's not None
        # Step 1 : Make the file name Unique
        new_filename = datetime.now().isoformat().replace(':', '_') + '.jpg'
        file.name = new_filename # Rename the name of file into newly created name
        save_uploaded_file('images', file) # Use save_uploaded_file() to save the renamed file


if __name__ == '__main__' :
    main()