import streamlit as st

from signup import signup_page
from test import test

def welcome_page():
    st.title("Welcome Page")
    st.write("Welcome to the app!")
    st.write("You have successfully signed up.")

if __name__ == "__main__":
    page = st.sidebar.selectbox("Page", ("Sign Up", "Welcome", "TEST"))
    if page == "Sign Up":
        signup_page()
    elif page == "Welcome":
        welcome_page()
    elif page == "TEST":
        test()
