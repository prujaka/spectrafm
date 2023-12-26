# SpectraFM: Discovering Similar Songs through Spectrograms

Welcome to SpectraFM, your tool for exploring the musical universe in a whole new dimension!

SpectraFM is a project designed to find similar songs by leveraging the power of spectrograms – visual representations of audio frequencies over time. Dive into the world of music analysis as we use modern techniques to compare and connect tunes on a spectral level.

## Features:

- **Versatile Data Source:** Utilizing the extensive FMA archive for a diverse musical journey.
- **Spectrogram Matching:** Explore songs based on their unique visual fingerprints.
- **Streamlit Frontend:** An intuitive and interactive user interface powered by Streamlit.

## Project Setup

The primary data source for this project is the [FMA archive](https://github.com/mdeff/fma), providing MP3 files and metadata. Begin by creating the necessary directories to store the data:

```zsh
mkdir -p data/mp3
mkdir -p data/png
```

The FMA archive offers MP3 audio data in various sizes: small (7.2 GB), medium (22 GB), large (93 GB), and full (879 GB). Execute the commands below to download the audio data and consolidate it into a single `data/mp3` folder:

```zsh
curl https://os.unil.cloud.switch.ch/fma/fma_small.zip --output fma_small.zip
tar xvf fma_small.zip --directory=data
find data/fma_small -mindepth 2 -type f -exec mv -i '{}' data/mp3 \;
rm -rf data/fma_small
rm fma_small.zip
```

In this example, we use the small one, but feel free to choose others: replace `fma_small` by `fma_medium`, `fma_large`, or `fma_full`. Additionally, the project utilizes FMA tracks metadata. To download and extract it, use the following commands:

```zsh
tar -xvf fma_metadata.zip -C data raw_tracks.csv
mv data/fma_metadata/raw_tracks.csv data
rmdir data/fma_metadata
```

With the data downloaded, the MP3 files are now ready for spectrogram generation. Use the preprocessing module of the project:

```zsh
python -m spectrafm.preprocessing
```

## Running the model

To utilize the model, run the web interface and follow the straightforward instructions on the opened page:

```zsh
streamlit run streamlit_app.py
```

## Conclusion

Thank you for exploring SpectraFM! I hope this tool adds a new dimension to your music discovery journey. If you have feedback, questions, or want to contribute, feel free to [reach out](sergeyprujina@gmail.com) or open an issue.

Happy listening!
