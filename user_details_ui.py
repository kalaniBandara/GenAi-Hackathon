import streamlit as st
from datetime import datetime

# Simulate data coming from the backend (replace with actual backend integration)
user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "dob": "1990-01-01",  # This is a string, we need to convert it
    "country": "United States",
    "language": "English",
    "health_literacy": "Intermediate",
    "username": "johndoe123",
    "password": "password123"  # For demo, but in a real app, store passwords securely!
}

# Convert the dob string to a datetime object
dob_as_date = datetime.strptime(user_data["dob"], "%Y-%m-%d").date()

# Store the edit mode in Streamlit session state
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

# Function to toggle edit mode
def toggle_edit():
    st.session_state.edit_mode = not st.session_state.edit_mode

# Create the User Detail Display UI
st.title("User Details")

# Check if in edit mode
if st.session_state.edit_mode:
    # Editable fields
    new_name = st.text_input("Full Name", value=user_data["name"])
    new_email = st.text_input("Email", value=user_data["email"])
    new_dob = st.date_input("Date of Birth", value=dob_as_date)  # Using the date object
    new_country = st.selectbox("Country", ["United States", "United Kingdom", "India", "New Zealand", "Australia", "Other"], index=["United States", "United Kingdom", "India", "New Zealand", "Australia", "Other"].index(user_data["country"]))
    new_language = st.selectbox("Preferred Language", ["English", "Spanish", "Mandarin", "Hindi", "Other"], index=["English", "Spanish", "Mandarin", "Hindi", "Other"].index(user_data["language"]))
    new_health_literacy = st.selectbox("Health Literacy Level", ["Beginner", "Intermediate", "Expert"], index=["Beginner", "Intermediate", "Expert"].index(user_data["health_literacy"]))
    new_username = st.text_input("Username", value=user_data["username"])
    new_password = st.text_input("Password", value=user_data["password"], type="password")

    # Save Changes Button
    if st.button("Save Changes"):
        # Update user data with new values (this is where you'd send data to the backend)
        user_data["name"] = new_name
        user_data["email"] = new_email
        user_data["dob"] = new_dob.strftime("%Y-%m-%d")  # Convert date back to string for storage
        user_data["country"] = new_country
        user_data["language"] = new_language
        user_data["health_literacy"] = new_health_literacy
        user_data["username"] = new_username
        user_data["password"] = new_password  # For demo purposes. Store securely in real apps!

        st.success("User details updated successfully!")

        # Exit edit mode after saving
        toggle_edit()

    # Cancel Button
    if st.button("Cancel"):
        # Exit edit mode without saving
        toggle_edit()

else:
    # Display user details in read-only mode
    st.write(f"**Name:** {user_data['name']}")
    st.write(f"**Email:** {user_data['email']}")
    st.write(f"**Date of Birth:** {user_data['dob']}")
    st.write(f"**Country:** {user_data['country']}")
    st.write(f"**Preferred Language:** {user_data['language']}")
    st.write(f"**Health Literacy Level:** {user_data['health_literacy']}")
    st.write(f"**Username:** {user_data['username']}")
    # Do not display the password, just mention it's saved
    st.write(f"**Password:** (hidden for security reasons)")

    # Edit Button
    if st.button("Edit"):
        toggle_edit()
