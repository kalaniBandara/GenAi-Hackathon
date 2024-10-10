import streamlit as st

# Create the signup form
st.title("User Signup")

name = st.text_input("Full Name")
email = st.text_input("Email")
dob = st.date_input("Date of Birth")
country = st.selectbox("Country", ["United States", "United Kingdom", "India", "New Zealand", "Australia", "Other"])
language = st.selectbox("Preferred Language", ["English", "Spanish", "Mandarin", "Hindi", "Other"])
health_literacy = st.selectbox("Health Literacy Level", ["Beginner", "Intermediate", "Expert"])
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    # Send the data to the backend here (the backend developer will implement this logic)
    st.success("User signed up successfully!")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Date of Birth: {dob}")
    st.write(f"Country: {country}")
    st.write(f"Preferred Language: {language}")
    st.write(f"Health Literacy: {health_literacy}")
    st.write(f"Username: {username}")
    # For security, it's best not to display the password back to the user
