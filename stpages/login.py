import streamlit as st
import tools
import time

def run():
	# Add the Login title
	st.title("Login")

	# Add the username and password input fields
	username = st.text_input("Username")
	password = st.text_input("Password", type="password")

	col1, col2 = st.columns((6,2.5))

	col2.button("Doesn't have an account?", on_click=tools.change_page('signup'))

	def reg():
		accounts = tools.Storage('accounts.json')
		# Check if the username and password are valid
		if accounts.get(username) == None:
			st.error("Invalid username or password. Please try again.")
		elif accounts.get(username).get('password') != password:
			st.error("Invalid username or password. Please try again.")
		else:
			st.success("Logged in successfully!")
			tools.change_page('ai')()
	# Add the login button
	col1.button("Login", on_click=reg)