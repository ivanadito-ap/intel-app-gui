import streamlit as st
from stpages import dashboard, signup, login
import tools
import remove_footer
# accounts = tools.Storage('accounts')
if __name__ == "__main__":
    # Initialization
    if 'page' not in st.session_state:
        st.set_page_config(page_title="AI Finance")
        st.session_state.page = 'dashboard'
    page = st.session_state.page
    if page == 'dashboard':
        dashboard.run()
    if page == 'signup':
        signup.run()
    if page == 'login':
        login.run()
    if page == 'signup' or page == 'login':
        st.sidebar.button("Introduction", on_click=tools.change_page('dashboard'))
    remove_footer.run()