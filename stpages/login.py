import streamlit as st
import tools

def run():
	# Add the Login title
	st.title("Login")

	# Add the username and password input fields
	username = st.text_input("Username")
	password = st.text_input("Password", type="password")

	col1, col2 = st.columns((6,2.5))

	col2.button("Doesn't have an account?", on_click=tools.change_page('signup'))
	# Add the login button
	if col1.button("Login"):
		accounts = tools.Storage('accounts.json')
		# Check if the username and password are valid
		if accounts.get(username) == None:
			st.error("Invalid username or password. Please try again.")
		elif accounts.get(username).get('password') != password:
			st.error("Invalid username or password. Please try again.")
		else:
			st.success("Logged in successfully!")