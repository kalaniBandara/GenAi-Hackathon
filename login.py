import streamlit as st

# Simulated user database (replace this with your actual user authentication system)
user_database = {
    "johndoe123": "password123",
    "janedoe456": "password456"
}

# Create the login form


# Add Bootstrap CSS
st.markdown(
    """
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True,
)

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .login-title {
        font-weight: bold;
        font-size: 24px;
        text-align: center;
        margin-bottom: 20px; /* Add some space below the title */
    }
    .login-form {
        max-width: 400px;
        margin: auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .logo {
        display: block;
        margin: auto;
        width: 150px;  /* Adjusted width for the logo */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the logo
st.image("D:/AWS Hackathon/GenAi-Hackathon/logo.png", use_column_width=False, width=150)

# Add a title with the custom CSS class
st.markdown('<div class="login-title">User Login</div>', unsafe_allow_html=True)

# Collect user input for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Layout for buttons (Login and Cancel side by side)
col1, col2 = st.columns([1, 1])

with col1:
    login_button = st.button("Login", key="login")

with col2:
    cancel_button = st.button("Cancel", key="cancel")

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
