# import libraries
import streamlit as st
from streamlit_supabase_auth import logout_button

# Access the session state
session_state = st.session_state

# Check if session_state is initialized
if hasattr(st, 'session_state'):

    # Check if 'id' and 'email' are present in session_state
    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 10_Help")
    else:
        print("session_state is not fully initialized - 10_Help")
        # Display a warning message and a login link
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()  # Stop the execution if not fully initialized
else:
    st.warning('Session_state not initialized. - 10_Helps')

# Set the title for the page
st.title("User Guidance")

# Create tabs for Help and Submit Feedback
tab1, tab2 = st.tabs(["Help", "Submit Feedback"])

# use tab1 for help
with tab1:
    # Define the content for the help section
    help_content = """
    ### Crop Yield Prediction Help

    Welcome to the Crop Yield Prediction app! This application assists in estimating crop production and making informed decisions related to agriculture.

    Here's a quick guide on how to use the app
    
    **1. Email Sign-Up and Confirmation**
    
    - Manually fill in the email and password fields on the sign-up page.
    
    - Click the "Sign-Up" button to submit the form.
    
    - Check the email inbox for the confirmation email.
    
    - Confirm that the email contains a valid confirmation link.
    
    - Click the confirmation link in the email.
    
    - Confirm that the link redirects to the sign-in page.
    
    - Manually fill in the email and password fields on the sign-in page.
    
    - Click the "Sign-In" button to submit the form.
    
    - Verify that the login is successful, and the user is redirected to the main application page.
    
    **2. Login via GitHub**
    
    - Click the "Login with GitHub" button.
    
    - If prompted, authorize the Crop Yield Prediction app on GitHub.
    
    - Verify that the login is successful, and the user is redirected to the main application page.
    
    **3. Login via Google**
    
    - Click the "Login with Google" button.
    
    - If prompted, authorize the Crop Yield Prediction app on Google.
    
    - Verify that the login is successful, and the user is redirected to the main application page.


    **4. Navigation**

    - **Homepage:** Start your journey on the homepage, where you'll find several sections including About, Dataset, Descriptive, Exploration, Preprocessing, Modeling, Report, and Help.
    
    - **Navigation Buttons:** Use the "Previous" and "Next" buttons in various sections to navigate seamlessly through the content.
    
    **5. About Section**

    Understand the purpose and significance of the application in the "About" section.
    Learn about the importance of accurate crop yield prediction and how the application aims to assist users.
    
    **6 Dataset Section**
    
    Access the "Dataset" section to explore the Indian Crop Yield dataset covering agriculture from 1997 to 2020.
    Utilize the "Download" option to obtain the dataset in CSV format.
    
    **7. Descriptive Section**

    Explore the "Descriptive" section to understand various metrics and statistical measures related to the dataset.
    Engage with visualizations, including density plots, to gain insights into laptop prices.
    
    **8. Exploration Section**

    Navigate to the "Exploration" section to visualize different distributions in the Indian Crop Yield dataset.
    Choose categories and visualizations using select boxes.
    
    **9. Data Cleaning and Preprocessing Section**

    Use the "Data Cleaning" section to handle missing values in the crop dataset.
    Select options such as "Drop," "Impute," and "Data Preprocessing" to refine the dataset.
    
    **10. Data Modeling and Evaluation Section**

    In the "Data Modeling" section, choose hyperparameters for the crop yield prediction model.
    Observe the training and evaluation process, and get real-time predictions for selected hyperparameters.

    **11. Crop Yield Report Section**

    Explore insights in the "Crop Yield Report" section, including statewise yield, annual rainfall, and fertilizer usage.
    Understand the impact of external factors, such as the COVID-19 lockdown, on agricultural metrics.
    
    **12. Help Section**

    Access the "Help" section for guidance on using the product and its features.
    Find information on each function and how to navigate through the application.

    **13. Search Functionality**

    Utilize the search functionality in various sections to quickly find specific information or details.

    **14. Submit Feedback**
    
    - **Step 1: Access the "Help" Section**

    Navigate to the "Help" section from the homepage. Look for the "Submit Feedback" tab option.
    
    - **Step 2: Click on "Submit Feedback"**

    Once you've located the "Submit Feedback" option, click on it to open the feedback submission form.

    - **Step 3: Fill in the Feedback Form**

    Complete the feedback form with details such as your name, email, and a detailed description of your feedback.
    
    - **Step 4: Submit Your Feedback**

    Once you've filled in the required details and attached any relevant files, click the "Submit" button to send us your feedback.

    **15. 503 Error Handling**

    The 503 Service Unavailable error is an indication that the server is temporarily unable to handle the request. While our Crop Yield Prediction application is designed to provide a seamless user experience, occasionally, server-related issues may arise. Here's how we handle the 503 error to ensure users are informed and can navigate the situation effectively:

    - **What 503 Error Means**

    The 503 error typically occurs when the server is undergoing maintenance, is overloaded, or is facing temporary issues that prevent it from fulfilling the request. Please try again ater some time.
    
    
    """

    # Custom CSS to style the Help button
    custom_css = """
    <style>
    #help_button {
        float: right;
        position: topRight;
        top: 1000px;
        right: 1000px;
        z-index: 1000;
        padding: 10px;
        background-color: #f44336;
        border: 1px solid #dcdcdc;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
    }
    </style>
    """

    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Create a Help button with Markdown
    help_button_html = "<div id='help_button'>Help</div>"
    help_button_clicked = st.markdown(help_button_html, unsafe_allow_html=True)

    # Display help content when the button is clicked
    if help_button_clicked.button("Help"):
        with st.expander("Help Section"):
            st.markdown(help_content)

# use tab2 for submit feedback
with tab2:
    st.header("Submit Your Feedback")

    feedback_form = """
    <form action="https://formsubmit.co/NYete@my.gcu.edu" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your feedback here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(feedback_form, unsafe_allow_html=True)


    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")

# Display the welcome message in the sidebar along with the logout button
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()


# use column for positioning next and previous button
col1, col2, col3, col4, col5 = st.columns(5)

# use col1 for previous button
with col1:

    st.page_link("pages/9_📜_Report.py", label="Previous", icon="⬅")

# use col5 for next button
with col5:

    st.page_link("pages/2_🏠_HomePage.py", label="Next", icon="➡")




