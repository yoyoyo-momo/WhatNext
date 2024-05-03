import streamlit as st
import json


def home():
    st.title('WHATNEXT')
<<<<<<< Updated upstream
    st.header('There are 4 ways to get recommendations:')

    st.subheader('1. Prompt Recommendation')
    st.text('In put your prompt here, and we will recommend songs for you!')
    st.text_input('Enter your prompt here:')
    st.button('Get prompt Recommendations')

    st.subheader('2. Feature Recommendation')
    danceability = st.slider('Danceability', min_value=0.0, max_value=1.0, value=0.5)
    energy = st.slider('Energy')
    valence = st.slider('Valence')
    mode = st.slider('Mode')

    
=======
    st.header('3 ways to get recommendations:')

    st.subheader(':books: **Prompt Recommendation**')
    prompt_options = st.multiselect(
        "Please describe your feeling or feature you want in the song:",
        ["Happy", "Sorrow", "Hype", "Blue"])
    
    age = st.slider("Your Age:", min_value=0, max_value=100, value=25)
    location = st.text_input("Location:", "Gym")
    mood = st.text_input("Your Current Mood:", "Happy")
    genre = st.text_input("Genre:", "Pop")
    requirement = st.text_input("Specific Requirements:", "I love pop music.")
    data = {"age":age, "location":location, "mood":mood, "genre":genre, "requirement":requirement}
    with open('data.json', 'w') as file:
        json.dump(data, file)    
>>>>>>> Stashed changes

    st.subheader('3. Playlist Recommendation')
    st.text_input('Enter your Playlist URL here:')
    st.button('Get playlist Recommendations')

    st.subheader('4. Song Recommendation')
    st.text_input('Enter your Song URL here:')
    st.button('Get song Recommendations')