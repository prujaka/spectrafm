import os
import random
import sys

import cv2
import librosa
import numpy as np

from audioread import NoBackendError
from skimage.io import imsave
from skimage.transform import resize
from soundfile import LibsndfileError

import spectrafm.parameters as params


def convert_audios_to_spectrograms(mp3_dir: str, png_dir: str,
                                   sampled: bool = False, k_: int = 10):
    """Convert all mp3 files in mp3_dir to spectrograms and save them
    as png files to png_dir"""
    mp3_files = [file for file in os.listdir(mp3_dir) if file.endswith('.mp3')]
    if sampled:
        mp3_files = random.sample(mp3_files, k=k_)
    total_files = len(mp3_files)
    print(f"\nSpectrogram calculation of mp3 files in {mp3_dir} started.\n"
          f"Saving to {png_dir}\n")

    for i, mp3_file in enumerate(mp3_files, 1):
        try:
            spec = mp3_to_spectrogram(os.path.join(mp3_dir, mp3_file))
            png_file = mp3_file.replace('.mp3', '.png')
            png_file_full = os.path.join(png_dir, png_file)
            imsave(png_file_full, spec.astype(np.uint8))

            progress = i / total_files * 100
            print(f"Processing {mp3_file}, {i}/{total_files}. "
                  f"Progress [{int(progress)}%]", end="\r")
            sys.stdout.flush()

        except LibsndfileError:
            print(f"File {mp3_file} skipped due to LibsndfileError, "
                  f"it's probably damaged")
        except NoBackendError:
            print(f"File {mp3_file} skipped due to NoBackendError, "
                  f"it's probably damaged")


def mp3_to_spectrogram(mp3_file: str):
    """Converts a single mp3 file to a png spectrogram"""
    # Load the mp3 file
    y, sr = librosa.load(mp3_file)

    # Calculate the Mel spectrogram
    spec = librosa.stft(y)
    spec_mag, _ = librosa.magphase(spec)
    mel_spec = librosa.feature.melspectrogram(S=spec_mag, sr=sr)
    spec_db = librosa.amplitude_to_db(abs(mel_spec))

    # Resize the spectrogram
    spec_resized = resize(spec_db, (128, 128))
    spec_resized = cv2.normalize(spec_resized, None, 255, 0, cv2.NORM_MINMAX,
                                 cv2.CV_8U)

    return spec_resized


if __name__ == "__main__":
    mp3_dir = params.LOCAL_MP3_DIR
    png_dir = params.LOCAL_PNG_DIR
    convert_audios_to_spectrograms(mp3_dir, png_dir)
    print('mp3 files successfully converted to png spectrograms.')
