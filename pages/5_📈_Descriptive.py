# import libraries
import streamlit as st
import pandas as pd
from streamlit_supabase_auth import logout_button

# Access the session state
session_state = st.session_state

# Check if session_state is initialized
if hasattr(st, 'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 5_Descriptive")
    else:
        print("session_state is not fully initialized - 5_Descriptive")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized. - 5_Descriptive')

# Title of the page
st.title('Descriptive Analysis')

# Load the dataset for descriptive analysis
crop = pd.read_csv("crop_data/crop_yield.csv")

# Generate descriptive statistics and display the table
df = crop.describe(include='all').T
st.write(df)

# Sidebar with welcome message and logout button
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

# Define columns
col1, col2, col3, col4, col5 = st.columns(5)

# Add page links to the columns
with col1:
    st.page_link("pages/4_📚_Dataset.py", label="Previous", icon="⬅")

with col5:
    st.page_link("pages/6_📊_Exploration.py", label="Next", icon="➡")