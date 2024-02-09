import streamlit as st
from PIL import Image
from gtts import gTTS
from io import BytesIO
import IPython.display as ipd
import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Assuming the script is in the repository root
base_directory = os.getcwd();
# Construct the relative path within the repository
about = os.path.join(base_directory,"pages","2_🌾_About.py")

st.set_page_config(
    page_title='Getting Started',
    page_icon=":seedling:",
)

st.title('Crop Yield Prediction ":seedling:"')
st.subheader('Empowering Agriculture with Precision')
st.sidebar.success("Please select a page above.")


image_url ='https://californiaagnet.com/wp-content/uploads/sites/13/2022/10/fruitveggies-850x491.jpeg'
st.image(image_url, width=700)


col1, col2, col2, col4, col5 = st.columns(5)



with col5:
    st.page_link(about, label="Next", icon="➡")



sound_file = BytesIO()
tts = gTTS('Add text-to-speech to your app', lang='en')
tts.write_to_fp(sound_file)
