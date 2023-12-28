import cv2
import os
import pandas as pd
import spectrafm.parameters as params
from spectrafm.utilities import song_dict, img_dict


def img_neighbors(ref_image, png_dir: str):
    """Returns 10 closest images in png_dir to ref_image"""
    ref_image = cv2.resize(ref_image, (128, 128))
    hist1 = cv2.calcHist([ref_image], [0], None, [128], [0, 128])

    # precompute histograms for all images in data folder
    histograms = {}
    for filename in os.listdir(png_dir):
        image = cv2.imread(os.path.join(png_dir, filename))
        image = cv2.resize(image, (128, 128))
        hist2 = cv2.calcHist([image], [0], None, [128], [0, 128])
        histograms[filename] = hist2

    # compare histograms and store distances in dictionary
    distances = {}
    for filename, hist2 in histograms.items():
        distance = cv2.compareHist(hist1, hist2, cv2.HISTCMP_INTERSECT)
        distances[filename] = distance

    # sort distances and return top 10 closest images
    sorted_distances = sorted(distances.items(),
                              key=lambda x: x[1],
                              reverse=True)
    closest_images = [x[0] for x in sorted_distances[0:10]]
    closest_images_paths = list(
        map(lambda x: os.path.join(png_dir, x), closest_images))

    return closest_images_paths


def predict_playlist(artist: str = 'Ed Askew', song: str = 'Castle Of Stars'):
    """Find 10 closest neighbors of the spectrogram of a given seed song
    to spectrograms of the songs in the png folder. Only single artist is
    supported. If the song is not in the dataset, return the song's name.

    Parameters
    ----------
    song : str
        Song's name.

    artist : str
        Artist's name.

    Returns
    -------
    neighbors : list of shape (n_neighbors,) of tuples of shape (2,) of str
        List of tuples of the closest songs. First element of a tuple is
        a song name, the second one is the artist(s).
    """

    raw_tracks_df = pd.read_csv(params.LOCAL_CSV_PATH)

    df = raw_tracks_df[['track_id', 'artist_name', 'track_title']]

    seed_song_df = df[(df['track_title'] == song) &
                      (df['artist_name'] == artist)]
    if seed_song_df.shape[0] == 0:
        print("No such a song in the dataset. Returning the user's entry.")
        return f'{song} by {artist}'

    # get the seed song's spectrogram from its id
    seed_song_id = seed_song_df.squeeze().to_dict()['track_id']
    seed_song_img_path = song_dict(seed_song_id, seed_song_df)['png_path']
    ref_img = cv2.imread(seed_song_img_path, cv2.IMREAD_GRAYSCALE)

    # build up the playlist of the closest songs
    closest_images = img_neighbors(ref_img, params.LOCAL_PNG_DIR)
    playlist = [img_dict(img, df) for img in closest_images]

    return playlist


if __name__ == '__main__':
    print(predict_playlist())
