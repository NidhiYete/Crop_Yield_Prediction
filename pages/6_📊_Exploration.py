# import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_supabase_auth import logout_button

# Access the session state
session_state = st.session_state

# Check if session_state is initialized
if hasattr(st, 'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 6_Exploration")
    else:
        print("session_state is not fully initialized - 6_Exploration")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized. - 6_Exploration')

# Title of the page
st.title("Exploration")

# Load the dataset for exploration
crop = pd.read_csv("crop_data/crop_yield.csv")

# Subheader
st.subheader(" Different Visual Distributions in the Indian Crop Yield Dataset")

# Assuming 'crop' is your DataFrame
yearly_yield = crop.groupby('Crop_Year').mean().reset_index()

# Define visualization categories
categories = {
    'Bar Plots': ['Crop Distribution', 'Season Distribution'],
    'Line Charts': ['Average Yield Over the Years', 'Average Area Used Over the Years',
                    'Annual Rainfall Over the Years', 'Fertilizers Used Over the Years',
                    'Pesticides Used Over the Years'],
    'Scatter Plots': ['Scatter Plot for Area Vs Yield', 'Scatter Plot for Annual Rainfall Vs Yield',
                      'Scatter Plot for Fertilizers Used Vs Yield', 'Scatter Plot for Pesticides Used Vs Yield'],
    'Heatmaps': ['Correlation Heatmap']
}

# Create select boxes for category and visualization
category = st.selectbox('Choose Category', list(categories.keys()))

visualization_options = categories[category]
visuals = st.selectbox('Choose Visualization', visualization_options)

# Plot based on user selection
if category == 'Bar Plots':
    if visuals == 'Crop Distribution':
        plot1 = pd.DataFrame(crop['Crop'].value_counts()).head(50)
        st.bar_chart(plot1)
    elif visuals == 'Season Distribution':
        plot2 = pd.DataFrame(crop['Season'].value_counts())
        st.bar_chart(plot2)
elif category == 'Line Charts':
    if visuals == 'Average Yield Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Yield'], use_container_width=True, color="#FF0000")
    elif visuals == 'Average Area Used Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Area'], use_container_width=True, color="#FF0000")
    elif visuals == 'Annual Rainfall Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Annual_Rainfall'], use_container_width=True, color="#FF0000")
    elif visuals == 'Fertilizers Used Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Fertilizer'], use_container_width=True, color="#FF0000")
    elif visuals == 'Pesticides Used Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Pesticide'], use_container_width=True, color="#FF0000")
elif category == 'Scatter Plots':
    if visuals == 'Scatter Plot for Area Vs Yield':
        st.scatter_chart(data=crop, x='Area', y='Yield')
    elif visuals == 'Scatter Plot for Annual Rainfall Vs Yield':
        st.scatter_chart(data=crop, x='Annual_Rainfall', y='Yield')
    elif visuals == 'Scatter Plot for Fertilizers Used Vs Yield':
        st.scatter_chart(data=crop, x='Fertilizer', y='Yield')
    elif visuals == 'Scatter Plot for Pesticides Used Vs Yield':
        st.scatter_chart(data=crop, x='Pesticide', y='Yield')
elif category == 'Heatmaps':
    if visuals == 'Correlation Heatmap':
        fig, ax = plt.subplots()
        sns.heatmap(yearly_yield.corr(), annot=True, linewidths=2, cmap="magma", ax=ax)
        st.pyplot(fig)

# Sidebar with welcome message and logout button
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

# Define columns
col1, col2, col3, col4, col5 = st.columns(5)

# Add page links to the columns
with col1:
    st.page_link("pages/5_📈_Descriptive.py", label="Previous", icon="⬅")

with col5:
    st.page_link("pages/7_🛠_Preprocessing.py", label="Next", icon="➡")









