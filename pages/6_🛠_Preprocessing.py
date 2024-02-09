import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import PowerTransformer, OneHotEncoder
from scipy.stats.mstats import winsorize
from sklearn.impute import SimpleImputer



# Load sample data
# Use caching to avoid reloading data on each interaction

crop = pd.read_csv("C:\\Nidhi\\crop\\crop_yield.csv")

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
        scaler = PowerTransformer(method = 'yeo-johnson')
        crop[numeric_features] = scaler.fit_transform(crop[numeric_features])

    # Encode categorical features if selected
    if encode_categorical:
        for feature in categorical_features:
            crop = pd.concat([crop, pd.get_dummies(crop[feature], prefix=feature, drop_first=True)], axis=1)
        crop = crop.drop(categorical_features, axis=1)

    return crop, original_crop

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



if __name__ == "__main__":
    main()


col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("C:\\Nidhi\\predictive_analysis\\pages\\5_📊_Exploration.py", label="Previous", icon="⬅")

with col5:

    st.page_link("C:\\Nidhi\\predictive_analysis\\pages\\7_🤖_Modeling.py", label="Next", icon="➡")


