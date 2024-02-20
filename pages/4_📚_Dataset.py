# import libraries
import streamlit as st
import pandas as pd
from streamlit_supabase_auth import logout_button

# Access the session state
session_state = st.session_state

# Check if session_state is initialized
if hasattr(st,'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 4_Dataset")
    else:
        print("session_state is not fully initialized - 4_Dataset")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized. - 4_Dataset')

# Title of the page
st.title('Dataset - Indian Crop Yield :chart_with_upwards_trend:')

# Introduction text about the dataset
st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The crop yield prediction dataset is accessible on Kaggle, covering Indian agriculture from 1997 to 2020. '
         'The comprehensive dataset, sourced from government outlets like District-wise Season-wise Crop Production '
         'Statistics, FAOSTAT, Rainfall India, Environics India, and IMD Pune, includes vital features for prediction.'
         ' These features encompass crop types, crop years, cropping seasons, states, cultivation areas, production '
         'quantities, annual rainfall, fertilizer and pesticide usage, and calculated yields. The structured data, '
         'presented in CSV format, consists of both qualitative (e.g., crop, state, season) and quantitative '
         '(e.g., crop_year, area, production, rainfall, fertilizer, pesticide usage, yield) information. The dataset '
         'contains 10 columns and 19,698 rows, representing data for various crops and their corresponding features '
         'over the specified period. ')

# Load and display the dataset
crop = pd.read_csv('crop_data/crop_yield.csv')
st.write(crop)

# Store the dataset in the session state for later use
st.session_state['crop'] = pd.read_csv('crop_data/crop_yield.csv')

# Sidebar with welcome message and logout button
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

# Define columns
col1, col2, col3, col4, col5 = st.columns(5)

# Add page links to the columns
with col1:
    st.page_link("pages/3_🌾_About.py", label="Previous", icon="⬅")

with col5:
    st.page_link("pages/5_📈_Descriptive.py", label="Next", icon="➡")