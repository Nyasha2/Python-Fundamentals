"""
CS 1 22fa
Lab 4: Dictionaries with Spotify

Credit: Leo Jenkins

Tests for Lab04 Exercise 3: find_average_audio_features
"""

from lab04 import find_average_audio_features
from lab04_backend import display_average_audio_features, load_tracks

if __name__ == '__main__':
    tracks = load_tracks()

    average_audio_features = find_average_audio_features(tracks)
    display_average_audio_features(average_audio_features)
