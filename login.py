import streamlit as st

# Simulated user database (replace this with your actual user authentication system)
user_database = {
    "johndoe123": "password123",
    "janedoe456": "password456"
}

# Create the login form
st.title("User Login")

# Collect user input for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Layout for buttons (Login and Cancel side by side)
col1, col2 = st.columns([1, 1])

with col1:
    login_button = st.button("Login")
    
with col2:
    cancel_button = st.button("Cancel")

# Handle login button click
if login_button:
    if username in user_database and user_database[username] == password:
        st.success(f"Welcome, {username}!")
    else:
        st.error("Invalid username or password. Please try again.")

# Handle cancel button click
if cancel_button:
    # Clear the input fields
    st.experimental_rerun()  # This will reload the app and reset the form
