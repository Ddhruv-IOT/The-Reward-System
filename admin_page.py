import streamlit as st
from streamlit_option_menu import option_menu
from add_user import add_user


def adm_page():
    # st.write("Admin Page")
    with st.sidebar:
        choose = option_menu(
            "RAIoT Rewards",
            ["Statics", "Add User", "Coming Soon!"],
            icons=["house", "camera fill", "kanban", "book", "person lines fill"],
            menu_icon="app-indicator",
            default_index=0,
        )

    if choose == "Add User":
        add_user()
