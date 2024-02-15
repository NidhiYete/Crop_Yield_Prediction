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

# display title
st.title("Crop Yield Prediction")

# Make container
select_features = st.container()

# load and read data
crop = pd.read_csv("crop_data/crop_yield.csv")

crop_df = crop.copy()
crop_df = crop_df.drop(['Crop_Year','Pesticide', 'Crop', 'State', 'Season'], axis = 1)
crop_df.head()
numeric_features = crop_df.select_dtypes(include=['int', 'float']).columns
categorical_features = crop_df.select_dtypes(include=['object']).columns


# Create a copy of the original data for comparison
original_crop = crop_df.copy()

# missing values
original_crop = original_crop.dropna()

# outliers
for feature in numeric_features:
    original_crop[feature] = winsorize(original_crop[feature], limits=[0.01, 0.01])

# get dummy variables
#crop_df = pd.get_dummies(original_crop, columns = categorical_features, drop_first=True)


# Splitting data into features (X) and target variable (y)
X = crop_df.drop('Yield', axis=1)
y = crop_df['Yield']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=123)

# Fit the scaler on the training set and transform both training and testing sets
# scaling
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert the scaled arrays back to DataFrames and assign column names
X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X_test.columns)

# Random Forest Regressor
rf_model = RandomForestRegressor()
rf_model.fit(X_train_scaled_df, y_train)


def user_input_features():
    with select_features:
        st.subheader("Please Choose Hyperparameters of the Model.")

        # select sliders
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
                'Fertilizer': crop_fert}

        features = pd.DataFrame(data, index=[0])
        return features

df = user_input_features()

st.subheader('Data Modeling and Evaluation')
st.sidebar.header("Choose Hyperparameters of the Models")

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


col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("pages/6_🛠_Preprocessing.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/8_📜_Report.py", label="Next", icon="➡")







