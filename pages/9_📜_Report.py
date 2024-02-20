# import libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_supabase_auth import logout_button

# Set the title for the report
st.title("Crop Yield Report")

# Access the session state
session_state = st.session_state

# Check if session_state is initialized
if hasattr(st, 'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 8_Report")
    else:
        print("session_state is not fully initialized - 8_Report")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized. -8_Report ')

# Read the crop yield data
crop = pd.read_csv("crop_data/crop_yield.csv")

# Group the data by state and calculate the sum of yield
crop_state = crop.groupby('State').sum()
crop_state.sort_values(by='Yield', inplace=True, ascending=False)

# Create tabs for different reports
tab1, tab2, tab3 = st.tabs(["Statewise Yield", "Statewise Annual Rainfall", "Statewise Fertilizer Usage"])

# Tab for Statewise Annual Rainfall
with tab2:
    st.subheader("Annual Rainfall in States of India")

    # Create an interactive bar chart with Plotly Express
    fig = px.bar(crop, x='State', y='Annual_Rainfall', color='State', hover_data=['Annual_Rainfall'])

    # Adjust the size of the plot if needed
    fig.update_layout(width=800, height=600)

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    # Additional information
    st.write("**The state of Meghalaya has the highest Annual Rainfall followed by the state West Bengal.**")

    # Additional markdown content
    st.markdown('In 2020, a noticeable downturn was evident across various agricultural metrics, encompassing crop yield,' 
        'cultivated area, and the utilization of pesticides and fertilizers. This decline is potentially linked to the' 
        'nationwide lockdown imposed in India in response to the COVID-19 virus, causing disruptions in agricultural' 
        'practices. Upon initial data examination, a positive skewness in the distribution of data features was observed.'
        'Following meticulous data cleaning and scaling procedures, a transformative process ensued, yielding a more'
        'normalized and linearly distributed dataset. This normalization holds paramount importance in ensuring the' 
        'reliability of subsequent statistical analyses and model performance. Subsequent assessments affirmed the' 
        'fulfillment of assumptions regarding linearity, independence, normality, and homoscedasticity in the data.'
        'More specifically, the features showcased a more symmetric distribution post-scaling, aligning with the' 
        'assumptions of normality. The lack of significant correlations among most features, except for the positive'
        'correlation noted between production and yield, and between Pesticide and Fertilizer substantiates the' 
        'assumption of independence among variables. These findings significantly contribute to fortifying the robustness'
        'of subsequent analyses and modeling endeavors within the agricultural dataset.')

# Tab for Statewise Yield
with tab1:
    st.subheader("Crop Yield in States of India")

    # Create an interactive bar chart with Plotly Express
    fig = px.bar(crop, x='State', y='Yield', color='State', hover_data=['Yield'])

    # Adjust the size of the plot if needed
    fig.update_layout(width=800, height=600)

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    # Additional information
    st.write("**In India, West Bengal produces the highest yield, followed by Puducherry and Andhra Pradesh.**")

    # Additional markdown content
    st.markdown('In 2020, a noticeable downturn was evident across various agricultural metrics, encompassing crop yield,' 
        'cultivated area, and the utilization of pesticides and fertilizers. This decline is potentially linked to the' 
        'nationwide lockdown imposed in India in response to the COVID-19 virus, causing disruptions in agricultural' 
        'practices. Upon initial data examination, a positive skewness in the distribution of data features was observed.'
        'Following meticulous data cleaning and scaling procedures, a transformative process ensued, yielding a more'
        'normalized and linearly distributed dataset. This normalization holds paramount importance in ensuring the' 
        'reliability of subsequent statistical analyses and model performance. Subsequent assessments affirmed the' 
        'fulfillment of assumptions regarding linearity, independence, normality, and homoscedasticity in the data.'
        'More specifically, the features showcased a more symmetric distribution post-scaling, aligning with the' 
        'assumptions of normality. The lack of significant correlations among most features, except for the positive'
        'correlation noted between production and yield, and between Pesticide and Fertilizer substantiates the' 
        'assumption of independence among variables. These findings significantly contribute to fortifying the robustness'
        'of subsequent analyses and modeling endeavors within the agricultural dataset.')

# Tab for Statewise Fertilizer Usage
with tab3:
    st.subheader("Fertilizer Usage in States of India")

    # Create an interactive bar chart with Plotly Express
    fig = px.bar(crop, x='State', y='Fertilizer', color='State', hover_data=['Fertilizer'])

    # Adjust the size of the plot if needed
    fig.update_layout(width=800, height=600)

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    # Additional information
    st.write("**Uttar Pradesh leads in the highest fertilizer usage, followed by Madhya Pradesh and Maharashtra in terms of quantity.**")

    # Additional markdown content
    st.markdown('In 2020, a noticeable downturn was evident across various agricultural metrics, encompassing crop yield,' 
        'cultivated area, and the utilization of pesticides and fertilizers. This decline is potentially linked to the' 
        'nationwide lockdown imposed in India in response to the COVID-19 virus, causing disruptions in agricultural' 
        'practices. Upon initial data examination, a positive skewness in the distribution of data features was observed.'
        'Following meticulous data cleaning and scaling procedures, a transformative process ensued, yielding a more'
        'normalized and linearly distributed dataset. This normalization holds paramount importance in ensuring the' 
        'reliability of subsequent statistical analyses and model performance. Subsequent assessments affirmed the' 
        'fulfillment of assumptions regarding linearity, independence, normality, and homoscedasticity in the data.'
        'More specifically, the features showcased a more symmetric distribution post-scaling, aligning with the' 
        'assumptions of normality. The lack of significant correlations among most features, except for the positive'
        'correlation noted between production and yield, and between Pesticide and Fertilizer substantiates the' 
        'assumption of independence among variables. These findings significantly contribute to fortifying the robustness'
        'of subsequent analyses and modeling endeavors within the agricultural dataset.')

# Sidebar and navigation
col1, col2, col3, col4, col5 = st.columns(5)

# Display the welcome message in the sidebar along with the logout button
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

# generate text report
text = '''In 2020, a noticeable downturn was evident across various agricultural metrics, encompassing crop yield, 
        cultivated area, and the utilization of pesticides and fertilizers. This decline is potentially linked to the 
        nationwide lockdown imposed in India in response to the COVID-19 virus, causing disruptions in agricultural 
        practices. Upon initial data examination, a positive skewness in the distribution of data features was observed.
        Following meticulous data cleaning and scaling procedures, a transformative process ensued, yielding a more 
        normalized and linearly distributed dataset. This normalization holds paramount importance in ensuring the 
        reliability of subsequent statistical analyses and model performance. Subsequent assessments affirmed the 
        fulfillment of assumptions regarding linearity, independence, normality, and homoscedasticity in the data.
        More specifically, the features showcased a more symmetric distribution post-scaling, aligning with the 
        assumptions of normality. The lack of significant correlations among most features, except for the positive 
        correlation noted between production and yield, and between Pesticide and Fertilizer substantiates the 
        assumption of independence among variables. These findings significantly contribute to fortifying the robustness
         of subsequent analyses and modeling endeavors within the agricultural dataset.'''

st.download_button('Download Text Report', text)

# Add page links to the columns

with col1:

    st.page_link("pages/8_🤖_Modeling.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/10_🤝_Help.py", label="Next", icon="➡")