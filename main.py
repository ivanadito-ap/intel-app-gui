import streamlit as st
from stpages import dashboard, signup, login, ai
import tools
import remove_footer
if __name__ == "__main__":
    # Initialization
    if 'page' not in st.session_state:
        st.set_page_config(page_title="AI Finance")
        st.session_state.page = 'dashboard'
    page = st.session_state.page
    if page == 'dashboard':
        dashboard.run()
    elif page == 'signup':
        signup.run()
    elif page == 'login':
        login.run()
    elif page == 'ai':
        ai.run()

    if page == 'signup' or page == 'login':
        st.sidebar.button("Introduction", on_click=tools.change_page('dashboard'))
    remove_footer.run()