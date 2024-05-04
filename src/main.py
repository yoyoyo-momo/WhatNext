import streamlit as st
from streamlit_option_menu import option_menu
from home import home
from about import about
from recommendations import recommendations


def menu():
    st.session_state.page = option_menu(None, ["Home", "Recommendations", "About"], 
    icons=['house', 'collection-play', "list-task"], 
    menu_icon="cast", default_index=0, orientation="horizontal")


def main():
    menu()
    if st.session_state.page == "Home":
        home()
    elif st.session_state.page == "Recommendations":
        recommendations()
    elif st.session_state.page == "About":
        about()

if __name__ == "__main__":
    main()