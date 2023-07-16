import streamlit as st


st.write("Please fill out the form below to sign up.")

# Input fields
full_name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")
terms_accepted = st.checkbox("I accept the terms and conditions")

# Sign-up button
if st.button("Sign Up"):
    if not full_name or not email or not password or not confirm_password:
        st.error("Please fill out all the fields.")
    elif password != confirm_password:
        st.error("Passwords do not match.")
    elif not terms_accepted:
        st.error("Please accept the terms and conditions.")
    else:
        # Perform sign-up logic here (e.g., store user details in a database)
        st.success("You have successfully signed up!")