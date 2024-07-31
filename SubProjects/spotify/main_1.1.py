"""
CS 1 22fa
Lab 4: Dictionaries with Spotify

Credit: Leo Jenkins

Tests for Lab04 Exercise 1: find_track_popularities
"""
from lab04 import find_track_popularities
from lab04_backend import display_track_popularities, load_tracks

if __name__ == '__main__':
    tracks = load_tracks()

    track_popularities = find_track_popularities(tracks)
    display_track_popularities(track_popularities)
