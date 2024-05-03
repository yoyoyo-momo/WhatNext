import streamlit as st

def about():
    st.subheader('ChatBox Tutorial')
    """
    1. Type in chat about what you want to listen to. E.g. "I want some music to dance to."
    2. Press "Enter".
    3. See your recommendation in the "Result" page.
    """
    st.video('Test_video.webm', loop=True, autoplay=True, muted=True)
    st.subheader('Audio Features Customization')
    """
    Customize your music recommendations by inputting your preferred feature values.
    """
    st.subheader('Audio Features Explanation')
    """
    | Variable | Description |
    | :----: | :---: |
    | Danceability | Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. |
    | Energy | Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy. |
    | Mode | Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0. |
    | Valence | A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). |
    """
    st.subheader('Playlist URL Explanation')
    """
    1. Copy your personal playlist url and paste it in the column.
    2. Press "Enter".
    3. See the generated playlist in the "Result" page. 
    """