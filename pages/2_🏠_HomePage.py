# import libraries
import streamlit as st
from gtts import gTTS
from io import BytesIO
import warnings
import os
warnings.filterwarnings("ignore")
from streamlit_supabase_auth import logout_button

# Set Streamlit page configuration
st.set_page_config(
    page_title='Getting Started',
    page_icon=":seedling:",
)

# Access the session state
session_state = st.session_state

# Logout function definition
def logoutfunct():
    print('Logout function called.')
    logout_button()

    # st.markdown('<meta http-equiv="refresh" content="2">', unsafe_allow_html=True)

# Check if session_state is initialized
if hasattr(st,'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 2_HomePage")
    else:
        print("session_state is not fully initialized - 2_HomePage")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized.')

# Main content of the page
st.title('Crop Yield Prediction ":seedling:"')
st.subheader('Empowering Agriculture with Precision')

# Display the welcome message in the sidebar along with the logout button
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logoutfunct()

# Display an image
image_url ='https://californiaagnet.com/wp-content/uploads/sites/13/2022/10/fruitveggies-850x491.jpeg'
st.image(image_url, width=700)

# Define columns
col1, col2, col3, col4, col5 = st.columns(5)

# Add a page link in one of the columns
with col5:
    st.page_link('pages/3_🌾_About.py', label="Next", icon="➡")

# Generate text-to-speech using gTTS
sound_file = BytesIO()
tts = gTTS('Add text-to-speech to your app', lang='en')
tts.write_to_fp(sound_file)