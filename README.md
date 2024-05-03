# Streamlit


## Dataset download
The dataset can be download in [here](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge/dataset_files).
After download the dataset, move the ```spotify_million_playlist_dataset``` and ```spotify_million_playlist_dataset_challenge``` under ````dset``` folder. Please create one if did not exist.

## Envornment Setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```
cd src
streamlit run main.py
```


## Referecne
The preprocess dataset is inspired from [Abdelrhman-Elruby](https://huggingface.co/spaces/Abdelrhman-Elruby/Spotify-Recommendation-System).