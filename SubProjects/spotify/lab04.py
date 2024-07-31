"""
CS 1 22fa
Student name: Nyasha
Lab Hour: 7pm-8pm
Lab 4: Dictionaries with Spotify

Credit: Leo Jenkins

Lab 04 Exercises, working with the Spotify API to process track and artist
data from a specified Spotify playlist.

Exercise 1. Track Popularity barchart (find_track_popularities)
Exercise 2. Genre Frequency Pie Chart (find_genre_frequencies)
Exercise 3. Audio Feature Analysis (find_average_audio_features)
"""

# If you want to analyze your personal playlist, follow the steps
# in the instructions to replace this link.
# playlist_link = 'https://open.spotify.com/playlist/5vvSGh2XdCVNcGvHFP8pMC?si=e8afeebd28a943bc'

# Here's the staff playlist link:
playlist_link = 'https://open.spotify.com/playlist/6R9ew7npRjmArdwfdA8vlG?si=dd2d64703e574af2'
# Here's the student playlist link (feel free to add your own songs!)
# playlist_link = 'https://open.spotify.com/playlist/5vvSGh2XdCVNcGvHFP8pMC?si=a90db31d0dd743c0'

from lab04_backend import get_sp

# SECTION 1: Track popularities
def find_track_popularities(tracks):
    # Hint: Use the debugger breakpoint or print the following line
    # to interact with the tracks argument in the Debug Console
    track_popularities = {}

    for track in tracks:
        track_name = track['name']
        track_pop = track['popularity']
        if track_pop != 0: # do not include tracks with zero popularity
           track_popularities[track_name] = track_pop

    return track_popularities


# SECTION 2: Genre frequencies
def find_genre_frequencies(tracks):
    genre_frequencies = {}
    # Get the Spotify API interface to retrieve real-time data about each
    # artist.
    sp = get_sp()

    for track in tracks:
        artist_uri = track['artist_uri']
        # Hint: Use the debugger or print statement on the following line
        # to interact with the artist_info dictionary
        artist_info = sp.artist(artist_uri)
        artist_genres = artist_info['genres']

        for genre in artist_genres:
            if genre not in genre_frequencies:
                genre_frequencies[genre] = 0
            genre_frequencies[genre] += 1

    return genre_frequencies


# SECTION 3: Audio features
def find_average_audio_features(tracks):
    TARGET_FEATURES = ['danceability', 'energy', 'speechiness', 'acousticness',
                       'instrumentalness', 'liveness', 'valence']
    audio_features = {}

    for track in tracks:
        # Get the unique Spotify URI identifier for the track
        track_uri = track['uri']

        for feature in TARGET_FEATURES:
            if feature not in audio_features:
                audio_features[feature] = 0
            audio_features[feature] += track[feature]

    average_audio_features = {}

    for feature, level in audio_features.items():
        average_audio_features[feature] = level/ len(tracks)

    return average_audio_features
    
