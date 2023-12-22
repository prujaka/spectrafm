import streamlit as st
from spectrafm.model import predict_playlist


def main():
    st.title('SpectraFM')
    with st.form(key='input_song'):
        st.write('Please input the artist and the song title:')
        artist_name = st.text_input('Artist name')
        track_title = st.text_input('Song title')
        st.form_submit_button('Submit')

    artist_name = 'Manudub'
    track_title = '21st Century Dub Cloud'
    st.text(f'For the test purposes, the song is {track_title} '
            f'by {artist_name}.')

    playlist = predict_playlist(artist=artist_name, song=track_title)

    for i, entry in enumerate(playlist, 1):
        st.text(f"{i}. {entry['artist_name']} - {entry['track_title']}")
        st.audio(entry['mp3_path'])
        st.image(entry['png_path'])


if __name__ == '__main__':
    main()
