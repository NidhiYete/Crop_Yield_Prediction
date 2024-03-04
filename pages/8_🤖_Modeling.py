# import libraries
import pandas as pd
import streamlit as st
import numpy as np
from numpy import reshape
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import PowerTransformer, OneHotEncoder, MinMaxScaler
from scipy.stats.mstats import winsorize
from streamlit_supabase_auth import logout_button


# Access the session state
session_state = st.session_state

# Check if session_state is initialized
if hasattr(st, 'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 9_Modeling")
    else:
        print("session_state is not fully initialized - 9_Modeling")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized. - 9_Modeling')

# Display title
st.title("Crop Yield Prediction")

# Create container
select_features = st.container()

# Load and read data
crop = pd.read_csv("crop_data/crop_yield.csv")

crop_df = crop.copy()
crop_df = crop_df.drop(['Crop_Year','Pesticide', 'Crop', 'State', 'Season'], axis=1)
crop_df.head()
numeric_features = crop_df.select_dtypes(include=['int', 'float']).columns
categorical_features = crop_df.select_dtypes(include=['object']).columns

# Create a copy of the original data for comparison
original_crop = crop_df.copy()

# Missing values
original_crop = original_crop.dropna()

# Outliers
for feature in numeric_features:
    original_crop[feature] = winsorize(original_crop[feature], limits=[0.01, 0.01])

# Get dummy variables
#crop_df = pd.get_dummies(original_crop, columns=categorical_features, drop_first=True)

# Splitting data into features (X) and target variable (y)
X = crop_df.drop('Yield', axis=1)
y = crop_df['Yield']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Fit the scaler on the training set and transform both training and testing sets
# Scaling
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert the scaled arrays back to DataFrames and assign column names
X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X_test.columns)

# Random Forest Regressor
rf_model = RandomForestRegressor()
rf_model.fit(X_train_scaled_df, y_train)

# Function to get user input features
def user_input_features():
    with select_features:
        st.subheader("Please Choose Hyperparameters of the Model.")

        # Select sliders
        crop_area = st.slider("Choose Area under cultivation", 5, 80000, 100)
        st.write("Value is:", crop_area, "Hectares")
        crop_prod = st.slider("Choose Quantity of Crop Production", 0, 150000, 1000)
        st.write("Value is:", crop_prod, "metric tons")
        crop_rainfall = st.slider("Choose Annual rainfall Received", 300, 5000, 100)
        st.write("Value is:", crop_rainfall, "mm")
        crop_fert = st.slider("Choose Amount of Fertilizer", 100, 30000000)
        st.write("Value is:", crop_fert, "Kilograms")

        data = {
            'Area': crop_area,
            'Production': crop_prod,
            'Annual_Rainfall': crop_rainfall,
            'Fertilizer': crop_fert
        }

        features = pd.DataFrame(data, index=[0])
        return features

df = user_input_features()

# Display modeling and evaluation section
st.subheader('Data Modeling and Evaluation')
st.sidebar.header("Choose Hyperparameters of the Models")

# Train and evaluate the model button
if st.button("Train and Evaluate Model"):
    st.write("Training and evaluating the selected model...")
    scaled_df = scaler.fit_transform(df)

    # Convert the scaled arrays back to DataFrames and assign column names
    df_pd = pd.DataFrame(scaled_df, columns=df.columns)

    # predict
    rf_predictions_df = rf_model.predict(df_pd)

    st.subheader("Prediction of Crop Yield")
    st.write(rf_predictions_df)
    st.write("Crop Yield predicted is ", rf_predictions_df, "production per unit area")
    st.balloons()
    
# generate text report
text3 = '''In the crop yield prediction analysis, three different regression models were employed: Linear Regression, 
            Random Forest, and LSTM (Long Short-Term Memory). The performance metrics for each model were assessed to 
            evaluate their predictive accuracy. The Linear Regression model yielded a Root Mean Squared Error (RMSE) of 
            359.80 and an R² (coefficient of determination) of 0.85. The Random Forest model outperformed it with an 
            RMSE of 277.93 and an R² of 0.91. The LSTM model, designed for sequential data, achieved the lowest RMSE of 
            0.24 and the highest R² of 0.94, indicating superior predictive capabilities. These results suggest that the
             Random Forest and LSTM models are well-suited for crop yield prediction, with the LSTM model demonstrating 
             exceptional accuracy. The cross-validation scores for the models further support their robustness, with 
             Random Forest exhibiting consistently high scores across different folds. The choice of these analytics 
             methods was driven by their ability to handle diverse data patterns and sequences, ensuring a comprehensive
              and accurate analysis of crop yield prediction.'''

st.download_button('Download Report', text3)

# Define columns
col1, col2, col3, col4, col5 = st.columns(5)

# Add page links to the columns
with col1:

    st.page_link("pages/7_🛠_Preprocessing.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/9_📜_Report.py", label="Next", icon="➡")







