import streamlit as st


def home():
    st.title('WHATNEXT')
    st.header('There are 4 ways to get recommendations:')

    st.subheader('1. Prompt Recommendation')
    st.text('In put your prompt here, and we will recommend songs for you!')
    text_input = st.text_input('Enter your prompt here:')
    st.button('Get Prompt Recommendations')

    st.subheader('2. Feature Recommendation')
    danceability = st.slider('Danceability', min_value=0.0, max_value=1.0, value=0.5)
    energy = st.slider('Energy', min_value=0.0, max_value=1.0, value=0.5)
    valence = st.slider('Valence', min_value=0.0, max_value=1.0, value=0.5)
    mode = st.slider('Mode', min_value=0.0, max_value=1.0, value=0.5)
    st.button('Get Feature Recommendations')

    

    st.subheader('3. Playlist Recommendation')
    st.text_input('Enter your Playlist URL here:')
    st.button('Get Playlist Recommendations')

    st.subheader('4. Song Recommendation')
    st.text_input('Enter your Song URL here:')
    st.button('Get Song Recommendations')