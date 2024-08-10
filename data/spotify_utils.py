import pandas  as pd
from typing import List
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyUtils:
    '''
    Utility class for getting data from spotify API and generating songs data

    Args:
        clinet_id (str): Client ID for the Spotify API
        clinet_secret (str): Client Secret for the Spotify API
    '''
    def __init__(self, clinet_id, clinet_secret):
        self.clinet = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clinet_id, client_secret=clinet_secret))

    def get_top_tracks_by_artist(self, artist_id: str) -> pd.DataFrame:
        '''
        Get top 10 tracks for every artist

        Args:
            artist_id (str): Spotify artist ID

        Returns:
            tracks_df (pd.DataFrame): Tracks data containing top song, album name, duration etc of an artist
        '''
        track_details = {
            "song_title": [],
            "album_name": [],
            "relase_date": [],
            "duration_ms": [],
            "song_id": []
        }
        tracks = self.clinet.artist_top_tracks(artist_id)['tracks']

        for track in tracks:
            track_details["song_id"].append(track["id"])
            track_details["duration_ms"].append(track["duration_ms"])
            track_details["song_title"].append(track["name"])
            track_details["album_name"].append(track["album"]["name"])
            track_details["relase_date"].append(track["album"]["release_date"])

        tracks_df = pd.DataFrame.from_dict(track_details)
        tracks_df["artist_id"] = artist_id
        return tracks_df

    