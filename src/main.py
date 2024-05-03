import streamlit as st
from streamlit_option_menu import option_menu
from home import home

st.title('WHATNEXT')


# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")


def menu():
    st.session_state.page = option_menu(None, ["Home", "Recommendations", "About"], 
    icons=['house', 'collection-play', "list-task"], 
    menu_icon="cast", default_index=0, orientation="horizontal")


def main():
    menu()
    if st.session_state.page == "Home":
        home()

if __name__ == "__main__":
    main()