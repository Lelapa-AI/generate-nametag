import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from test2 import draw_namecard

# Streamlit app
st.title('Name Tag Generator')
# Set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F9C400;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input for name
name = st.text_input('Enter your name:')
affil = st.text_input('Enter your affiliation:')
if name and affil:
    # Generate image
    img, img_path = draw_namecard(name, affil)
    
    # Display images
    st.image(img, caption='Generated Name Tag',)
    
    # Provide download link
    with open(img_path, "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name=img_path,
            mime="image/png"
        )
    
    name, affil = None, None