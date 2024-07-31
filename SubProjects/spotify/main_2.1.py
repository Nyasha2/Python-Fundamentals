"""
CS 1 22fa
Lab 4: Dictionaries with Spotify

Credit: Leo Jenkins

Tests for Lab04 Exercise 2: find_genre_frequencies
"""

from lab04 import find_genre_frequencies
from lab04_backend import display_genre_frequencies, load_tracks

if __name__ == '__main__':
    tracks = load_tracks()

    genre_frequencies = find_genre_frequencies(tracks)
    display_genre_frequencies(genre_frequencies)
