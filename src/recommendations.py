import streamlit as st
from model import song_model, playlist_model, prompt_model
import streamlit.components.v1 as components
from time import sleep


def recommendations():
    st.title('WHATNEXT')
    if "result_list" not in st.session_state:
        st.session_state.result_list = {}
        return

    print(len(st.session_state.result_list))
    print(type(st.session_state.result_list))

    iteration = 0
    for index, key in enumerate(st.session_state.result_list):
        display_url = "https://open.spotify.com/embed/track/" + key + "?utm_source=generator&theme=0"
        components.iframe(display_url, width=700, height=100)

        iteration += 1
        if iteration % 5 == 0:
            sleep(1)


def song_recommendations():
    st.session_state.result_list, error_msg = song_model(st.session_state.song_url, model="Spotify Model")


def playlist_recommendations():
    st.session_state.result_list, error_msg = playlist_model(st.session_state.playlist_url, model="Spotify Model")


def prompt_recommendations():
    st.session_state.result_list, error_msg = prompt_model()