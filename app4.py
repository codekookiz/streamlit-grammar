"""
# To show image, video, and music file on webpage
"""

import streamlit as st

# Import library for Image Process
from PIL import Image

def main() :
    # Step 1 : Display local image file on the webpage
    img = Image.open('data/image_03.jpg') # To bring image file from specific directory
    st.image(img, width = 500) # Show loaded image on the webpage
    st.image(img, use_container_width = True) # Fit the image size with the webpage size

    # Step 2 : Display image file from Internet on the webpage
    url = 'https://yt3.googleusercontent.com/ytc/AIdro_kt5wWyx5mgGt4M76y87ArgV-_jyEGiONOZ8hOf94tPwZQ=s900-c-k-c0x00ffffff-no-rj'
    st.image(url, width = 300)

    # Step 3 : Display local video file on the webpage
    video_file = open('data/video1.mp4', 'rb') # 'r' means 'Read', 'b' means 'Binary File', 't' means 'Text file'
    st.video(video_file, format = 'video/mp4') # format : The extension of the file; not necessary cuz code automatically recognizes it

    # Step 4 : Display local audio file on the webpage
    sound_file = open('data/song.mp3', 'rb')
    st.audio(sound_file, format = 'audio/mp3')


if __name__ == '__main__' :
    main()