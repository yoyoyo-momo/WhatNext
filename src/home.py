import streamlit as st
from recommendations import song_recommendations, playlist_recommendations
import json


def home():
    st.title('WHATNEXT')
    st.header('3 ways to get recommendations:')

    st.subheader(':books: **Prompt Recommendation**')
    
    age = st.slider("Your Age:", min_value=0, max_value=100, value=25)
    location = st.text_input("Location:", "Gym")
    mood = st.text_input("Your Current Mood:", "Happy")
    genre = st.text_input("Genre:", "Pop")
    requirement = st.text_input("Specific Requirements:", "I love pop music.")
    data = {"age":age, "location":location, "mood":mood, "genre":genre, "requirement":requirement}
    with open('data.json', 'w') as file:
        json.dump(data, file)    

    st.subheader(':notes: **Playlist Recommendation**')
    st.session_state.playlist_url =  st.text_input('Enter your Playlist URL here:')
    st.button('Get Playlist Recommendations', on_click=playlist_recommendations)

    st.subheader(':musical_score: **Song Recommendation**')
    st.session_state.song_url = st.text_input('Enter your Song URL here:')
    st.button('Get Song Recommendations', on_click=song_recommendations)