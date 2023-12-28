import streamlit as st
from spectrafm.utilities import sample_songs
from spectrafm.model import predict_playlist


def main():
    st.title("SpectraFM: Discovering Similar Songs through Spectrograms")
    st.markdown("As a demonstration prototype, this tool uses the "
                "Free Music Archive songs, which may not be as widely "
                "recognized. To get started, "
                "here are some suggestions from the downloaded database. "
                "Feel free to copy one and input it into the form below.")
    sample = sample_songs()
    st.markdown("Examples:")
    st.table(sample)
    with st.form(key='input_song'):
        st.markdown("Please input the artist and the song title:")
        artist_name = st.text_input("Artist name")
        track_title = st.text_input("Song title")
        st.form_submit_button("Submit")

    artist_name = "Manudub"
    track_title = "21st Century Dub Cloud"
    st.markdown(f"For the test purposes, the song is {track_title} "
                f"by {artist_name}.")

    playlist = predict_playlist(artist=artist_name, song=track_title)

    for i, entry in enumerate(playlist, 1):
        st.markdown(f"{i}. {entry['artist_name']} - {entry['track_title']}")
        st.audio(entry['mp3_path'])
        st.image(entry['png_path'])


if __name__ == '__main__':
    main()
