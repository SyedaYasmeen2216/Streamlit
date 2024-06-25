import streamlit as st
from datetime import datetime
import time

# Function to handle login
def login(username, password):
    # Example credentials
    if username == "user" and password == "pass":
        return True
    else:
        return False

# Main application function
def main():
    st.set_page_config(page_title="Interactive Streamlit App", layout="wide")
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""

    if not st.session_state.logged_in:
        login_section()
    else:
        st.sidebar.title("Menu")
        app_section()

# Login Section
def login_section():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.error("Incorrect username or password")

# Main Application Section
def app_section():
    st.title(f"Welcome, {st.session_state.username}!")
    
    profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
    if profile_picture is not None:
        st.image(profile_picture, caption="Profile Picture", use_column_width=True)
    
    st.subheader("Select Date and Time")
    date = st.date_input("Select a date")
    time_input = st.time_input("Select a time")
    
    if st.button("Submit"):
        st.spinner(text="Processing...")
        time.sleep(1)  # Simulate a long computation
        st.success(f"Selected Date and Time: {date} {time_input}")

    st.subheader("Dynamic Text Size Adjustment")
    text_size = st.slider("Adjust text size", 10, 50, 20)
    st.markdown(f"<div style='font-size: {text_size}px;'>This text size is adjustable!</div>", unsafe_allow_html=True)
    
    st.subheader("Additional Information")
    if st.checkbox("Show/Hide"):
        st.write("Here is some additional information that you can show or hide.")

# Run the application
if __name__ == "__main__":
    main()
