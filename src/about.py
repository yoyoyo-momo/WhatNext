import streamlit as st

def about():
    st.subheader('Prompt Recommendation Tutorial')
    st.markdown("""
                1. Type in your information and press "Enter".
                2. After you finish, click on "Get Prompt Recommendations".
                2. See your recommendations in the "Recommendations" page.
                """)

    st.subheader('Playlist URL Tutorial')
    st.markdown("""
    1. Copy and paste your personal playlist url.
    2. Press "Get Playlist Recommendations".
    3. See the generated playlist in the "Recommendations" page. 
    """)

    st.subheader('Song URL Tutorial')
    st.markdown("""
    1. Copy and paste your own song url.
    2. Press "Get Song Recommendations".
    3. See the generated playlist in the "Recommendations" page. 
    """)