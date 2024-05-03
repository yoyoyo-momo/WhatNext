import streamlit as st


def home():
    st.subheader('1. Prompt Recommendation')
    st.text('In put your prompt here, and we will recommend songs for you!')
    st.text_input('Enter your text here:')
    st.button('Enter')

    st.subheader('2. Feature recommendation')
    danceability = st.slider('Danceability')
    energy = st.slider('Energy')
    valence = st.slider('Valence')
    mode = st.slider('Mode')

    

    st.subheader('3. Playlist Recommendation')

    st.subheader('4. Song Recommendation')