import streamlit as st
from recommendations import song_recommendations, playlist_recommendations

def home():
    st.title('WHATNEXT')
    st.header('3 ways to get recommendations:')

    st.subheader(':books: **Prompt Recommendation**')
    prompt_options = st.multiselect(
        "Please describe your feeling or feature you want in the song:",
        ["Happy", "Sorrow", "Hype", "Blue"])
    
    prompt_text = ""
    if prompt_options:
        prompt_text = "Give me some music that makes me feel "
    for i in prompt_options:
        prompt_text += i + " "

    st.text('In put your prompt here, and we will recommend songs for you!')
    text_area = st.text_area('Enter your prompt here:', 
                             prompt_text)
    st.button('Get Prompt Recommendations')

    # st.subheader('2. Feature Recommendation')
    # danceability = st.slider('Danceability', min_value=0.0, max_value=1.0, value=0.5)
    # energy = st.slider('Energy', min_value=0.0, max_value=1.0, value=0.5)
    # valence = st.slider('Valence', min_value=0.0, max_value=1.0, value=0.5)
    # mode = st.slider('Mode', min_value=0.0, max_value=1.0, value=0.5)
    # st.button('Get Feature Recommendations')

    

    st.subheader(':notes: **Playlist Recommendation**')
    st.session_state.playlist_url =  st.text_input('Enter your Playlist URL here:')
    st.button('Get Playlist Recommendations', on_click=playlist_recommendations)

    st.subheader(':musical_score: **Song Recommendation**')
    st.session_state.song_url = st.text_input('Enter your Song URL here:')
    st.button('Get Song Recommendations', on_click=song_recommendations)