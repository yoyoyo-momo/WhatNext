import streamlit as st

def about():
    st.subheader('Prompt Recommendation Tutorial')
    st.markdown("""
                1. Type in your information and press "Enter".
                2. After you finish, click on "Get Recommendations Through Prompt".
                2. See your recommendations in the "Recommendations" page.
                """)
    st.video('Test_video.webm', loop=True, autoplay=True, muted=True)

    st.subheader('Playlist URL Explanation')
    st.markdown("""
    1. Copy your personal playlist url and paste it in the column.
    2. Press "Get playlist Recommendations".
    3. See the generated playlist in the "Recommendations" page. 
    """)

    st.subheader('Song URL Explanation')
    st.markdown("""
    1. Copy your own song url and paste it in the column.
    2. Press "Get song Recommendations".
    3. See the generated playlist in the "Recommendations" page. 
    """)