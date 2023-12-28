import os
import pandas as pd

import spectrafm.parameters as params


def img_id(img_path_: str):
    """Given the path of a png file, returns the track id"""
    return int(img_path_.split('/')[-1].split('.')[0])


def img_path(song_id: int):
    """Given the track id, returns the path of a png file"""
    return os.path.join(params.LOCAL_PNG_DIR, f'{song_id:06}.png')


def song_dict(song_id: int, df: pd.DataFrame):
    """Given the song's id, returns a dictionary containing
    the track_id, the artist name, the song name, the mp3 file path
    and the spectrogram path"""
    d = df[df['track_id'] == 'track_id'].squeeze(axis=0).to_dict()
    d['png_path'] = img_path(song_id)
    d['mp3_path'] = d['png_path'].replace('/png', '/mp3').replace('.png',
                                                                  '.mp3')
    return d


def img_dict(img_path_: str, df: pd.DataFrame):
    """Given the song's spectrogram's path, returns a dictionary containing
    the track_id, the artist name, the song name, the mp3 file path
    and the spectrogram path"""

    track_id = img_id(img_path_)
    d = df[df['track_id'] == track_id].squeeze(axis=0).to_dict()
    d['png_path'] = img_path_
    d['mp3_path'] = img_path_.replace('/png', '/mp3').replace('.png', '.mp3')
    return d


def sample_songs(n_: int = 10):
    """Generate a random sample of songs from the 'data/raw_tracks.csv'.
    This function considers only those songs whose spectrograms are present in
    the 'data/png' directory. The sample is randomly selected.

    Parameters
    ----------
    n_ : int, optional (default=10)
        The number of songs to include in the sample.

    Returns
    -------
    DataFrame
        A DataFrame containing a random sample of songs. The DataFrame
        includes columns 'artist_name' and 'track_title'.

    Examples
    --------
    >>> sample = sample_songs(n_=5)
    >>> print(sample)
        artist_name           track_title
    0       Artist1          Sample Song1
    1       Artist2          Sample Song2
    2       Artist3          Sample Song3
    3       Artist4          Sample Song4
    4       Artist5          Sample Song5

    """
    df_full = pd.read_csv('data/raw_tracks.csv')
    png_dir_files = os.listdir('data/png')
    png_files = [file for file in png_dir_files if file.endswith('.png')]

    ids = sorted([int(file.split('.')[0]) for file in png_files])
    df = df_full.loc[df_full['track_id'].isin(ids)]

    sample = df[['artist_name', 'track_title']].sample(n=n_).reset_index(
        drop=True)
    sample.index = range(1, n_ + 1)
    sample = sample.rename(columns={'artist_name': 'Artist name',
                                    'track_title': 'Track title'})
    return sample
