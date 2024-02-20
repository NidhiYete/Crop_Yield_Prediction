# import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import PowerTransformer, OneHotEncoder
from scipy.stats.mstats import winsorize
from sklearn.impute import SimpleImputer
from streamlit_supabase_auth import logout_button

# Access the session state
session_state = st.session_state

# Check if session_state is initialized
if hasattr(st, 'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 7_Preprocessing")
    else:
        print("session_state is not fully initialized - 7_Preprocessing")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized. - 7_Preprocessing')

# Load the crop data
crop = pd.read_csv("crop_data/crop_yield.csv")

# Function to clean and preprocess data
@st.cache_data(show_spinner=False)
def clean_data(crop, handle_missing, winsorize_outliers, scale_numerical, encode_categorical):
    # Data cleaning and preprocessing
    numeric_features = crop.select_dtypes(include=['int', 'float']).columns
    categorical_features = crop.select_dtypes(include=['object']).columns

    # Create a copy of the original data for comparison
    original_crop = crop.copy()

    # Drop or impute missing values based on user choice
    if handle_missing == 'Drop':
        crop = crop.dropna()
    elif handle_missing == 'Impute':
        imputer = SimpleImputer(strategy='mean')
        crop[numeric_features] = imputer.fit_transform(crop[numeric_features])

    # Winsorize outliers if selected
    if winsorize_outliers:
        for feature in numeric_features:
            crop[feature] = winsorize(crop[feature], limits=[0.01, 0.01])  # Adjust the limits as needed

    # Scale numerical features if selected
    if scale_numerical:
        scaler = PowerTransformer(method='yeo-johnson')
        crop[numeric_features] = scaler.fit_transform(crop[numeric_features])

    # Encode categorical features if selected
    if encode_categorical:
        for feature in categorical_features:
            crop = pd.concat([crop, pd.get_dummies(crop[feature], prefix=feature, drop_first=True)], axis=1)
        crop = crop.drop(categorical_features, axis=1)

    return crop, original_crop

# Main function
def main():
    st.title('Crop Data Cleaning and Preprocessing ')

    # User input options for cleaning
    st.sidebar.header("**Data Cleaning**")
    handle_missing = st.sidebar.radio('**Handle Missing Values**', ['Drop', 'Impute'])
    winsorize_outliers = st.sidebar.checkbox('Winsorize Outliers')
    st.sidebar.header("**Data Preprocessing**")
    scale_numerical = st.sidebar.checkbox('Scale Numerical Features')
    encode_categorical = st.sidebar.checkbox('Encode Categorical Features')

    # Clean and preprocess the data
    cleaned_crop, original_crop = clean_data(crop, handle_missing, winsorize_outliers, scale_numerical, encode_categorical)

    # Display original data for comparison
    st.subheader('Original Crop Data')
    st.write(original_crop)

    # Display cleaned and preprocessed data
    st.subheader('Cleaned and Preprocessed Crop Data')
    st.write(cleaned_crop)

# Execute the main function
if __name__ == "__main__":
    main()

# Sidebar with welcome message and logout button
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

# Define columns
col1, col2, col3, col4, col5 = st.columns(5)

# Add page links to the columns
with col1:
    st.page_link("pages/6_📊_Exploration.py", label="Previous", icon="⬅")

with col5:
    st.page_link("pages/8_🤖_Modeling.py", label="Next", icon="➡")

