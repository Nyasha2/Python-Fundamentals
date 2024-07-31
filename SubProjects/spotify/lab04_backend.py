"""
CS 1 22fa
Lab 4: Dictionaries with Spotify

Credit: Leo Jenkins
lab04_backend.py

This program provides the backend for Lab04, allowing users to generate
data visualizations for Spotify playlists. Requires lab04.py to be implemented
for the following visualization features:

1. Track Popularity barchart (find_track_popularities)
2. Genre Frequency Pie Chart (find_genre_frequencies)
3. Audio Feature Analysis (find_average_audio_features)
"""

import csv
# Spotify API imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Data analysis/visualization libraries
import matplotlib.pyplot as plt
import numpy as np
# from lab04 import playlist_link

# Replace this with your desired playlist link if you want to use your own.
# playlist_link = "https://open.spotify.com/playlist/5vvSGh2XdCVNcGvHFP8pMC?si=e8afeebd28a943bc"

# Here's the staff playlist link:
playlist_link = 'https://open.spotify.com/playlist/6R9ew7npRjmArdwfdA8vlG?si=dd2d64703e574af2'
# Here's the student playlist link (feel free to add your own songs!)
# playlist_link = 'https://open.spotify.com/playlist/5vvSGh2XdCVNcGvHFP8pMC?si=a90db31d0dd743c0'

# Spotify API credentials required to connect to Spotify API
CLIENT_ID = "9a5da0723f56439e90ad9128658d636f"
CLIENT_SECRET = "63c3d2e2ecf145d4b86965697785cc6b"

# Constants for track columns and target features
TRACK_COLUMNS = ['name', 'href', 'uri', 'popularity', 'album_name',
                 'release_date', 'album_uri', 'artist_name',
                 'artist_uri', 'genres']
TARGET_FEATURES = ['danceability', 'energy', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence']


#  API Connection
def get_sp():
    """
    Connects to Spotify API with credentials, returning a connected spotipy
    interface.
    """
    client_creds = SpotifyClientCredentials(client_id=CLIENT_ID,
                                            client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_creds)
    return sp


def display_track_popularities(track_popularities):
    """
    Given a (str -> str) dictionary of track popularities, generates a bar
    chart comparing popularity scores for different tracks.

    Each key in the dictionary should be a track name string mapping to a
    popularity value.

    Note: `track_popularities` will be a (name -> popularity) dict returned by
    lab04.find_track_popularities.
    """

    # Sort the dictionary of popularities in reverse order for the bar
    # chart.
    track_popularities = dict(sorted(track_popularities.items(),
                                     key=lambda item: item[1], reverse=True))

    songs = track_popularities.keys()
    popularities = track_popularities.values()

    plt.figure(figsize=(8, 5))

    # Settings for barchart
    plt.bar(songs, popularities, color="blue", width=0.6)
    plt.xlabel('Songs')
    plt.ylabel('Popularity')
    plt.title('Popularity by song')
    plt.xticks([])
    plt.show()


def display_genre_frequencies(genre_frequencies):
    """
    Given a (str -> str) dictionary of genre frequencies, generates a pie chart
    breaking down genre frequency ratios for a Spotify playlist.

    Each key in the dictionary should be a genre name string mapping to a
    frequency value.

    Note: `genre_frequencies` will be a (genre -> count) dict returned by
    lab04.find_genre_frequencies.
    """

    # Sort the dictionary of genre frequencies in reverse order for the pie
    # chart.
    genre_frequencies = dict(sorted(genre_frequencies.items(),
                                    key=lambda item: item[1], reverse=True))
    frequencies = genre_frequencies.values()
    labels = genre_frequencies.keys()

    fig = plt.figure(4, figsize=(8, 7))
    # 211 represents the position of the plot
    ax = fig.add_subplot(211)
    ax.set_title('Playlist Genre Frequencies')
    # Set equal scaling
    ax.axis('equal')

    # Create the pie chart given genre frequency values
    pie = ax.pie(frequencies)
    ax2 = fig.add_subplot(212)
    ax2.axis('off')
    # Render the pie chart legend
    ax2.legend(pie[0], labels, loc='center', ncol=3)
    plt.show()


def display_average_audio_features(average_audio_features):
    """
    Given a (str -> str) dictionary of audio features, generates a graph
    breaking down TARGET_FEATURES.

    Each key in the dictionary should be a track name string mapping to a
    popularity value.

    Note: `average_audio_features` will be a (feature -> feature_value) dict
    returned by lab04.find_average_audio_features.
    """
    labels = average_audio_features.keys()
    # filter out the feature values
    features = [average_audio_features[x] for x in labels]
    avg_features = [0.5913235828121778, 0.5913235828121778,
                    0.5913235828121778, 0.25545374859416076,
                    0.5913235828121778, 0.1914127261952776, 0.5913235828121778]

    # Returns evenly spaced intervals
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    fig = plt.figure(figsize=(25, 10))
    # Set the figure size dimensions in inches
    fig.set_size_inches((8, 8))

    # Create a polar subplot to generate a circular breakdown of audio
    # features
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, features, 'o-', linewidth=2,
            label='Features', color='blue')
    ax.plot(angles, avg_features, 'o-', linewidth=1,
            label='Average Features', color='gray')
    ax.fill(angles, features, alpha=0.25, facecolor='blue')
    ax.fill(angles, avg_features, alpha=0.15, facecolor='gray')
    ax.set_thetagrids(angles * 180/np.pi, labels, fontsize=13)

    ax.set_rlabel_position(180)
    # Position yticks
    plt.yticks([0.1 * x for x in range(1, 11)],
               [f'{0.1 * x:.1f}' for x in range(1, 11)], size=12)
    plt.ylim(0, 1.0)

    ax.set_title('Playlist Audio Features')
    # Configure grid lines
    ax.grid(True)

    plt.legend(loc='best', bbox_to_anchor=(0.1, 0.1))
    plt.show()


def gen_csv():
    """
    A utility function to generate a playlist CSV file given a
    student's playlist link of interest. Writes a new file in the form
    playlist_<playlist_uri>.csv, with columns being a merge of
    TARGET_FEATURES and TRACK_COLUMNS.

    Students don't need to update anything here, since it factors out more
    complicated logic using spotipy and API credentials, which we
    haven't taught.
    """

    # Get the URI from the link
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]

    sp = get_sp()
    # Fetch playlist data given the playlist URI identifier
    playlist_data = sp.playlist(playlist_URI)
    playlist_name = playlist_data['name']

    tracks = playlist_data['tracks']['items']
    # sp.playlist_tracks(playlist_URI)["items"]]
    track_uris = [x["track"]["uri"] for x in tracks]
    cleaned_tracks = []
    for track in tracks:
        cleaned_tracks.append(track['track'])

    playlist_name = clean_playlist_name(playlist_name)
    new_csv = f'playlist_{playlist_name}.csv'

    # Write playlist data (each track is a row) to new file
    with open(new_csv, 'w') as new_file:
        writer = csv.DictWriter(new_file,
                                fieldnames=(TRACK_COLUMNS + TARGET_FEATURES))
        # Flush the header to the new CSV file
        writer.writeheader()
        for track in cleaned_tracks:
            row_data = {
                'name': track['name'],
                'href': track['href'],
                'uri': track['uri'],
                'popularity': track['popularity'],
                'album_name': track['album']['name']
                if 'album' in track and
                   'name' in track['album'] else None,
                'release_date': track['album']['release_date']
                if 'album' in track and
                   'release_date' in track['album'] else None,
                'album_uri': track['album']['uri']
                if 'album' in track and
                   'uri' in track['album'] else None
            }
            # Next, add artist data using the first artist in the list of
            # artists associated with the track (in case there are multiple)
            if 'artists' in track and len(track['artists']) > 0:
                first_artist = track['artists'][0]
                row_data['artist_name'] = first_artist['name']
                row_data['artist_uri'] = first_artist['uri']
            else:
                row_data['artist_name'] = None
                row_data['artist_uri'] = None

            # Collect data about the artists' genres
            artist_uri = first_artist['uri']
            artist_info = sp.artist(artist_uri)
            row_data['genres'] = artist_info['genres']

            # Use the track's URI to fetch data for audio features
            track_uri = track["uri"]
            track_audio_features = sp.audio_features(track_uri)[0]

            for feature, level in track_audio_features.items():
                if feature in TARGET_FEATURES:
                    row_data[feature] = level

            # Finally, write everything as a track row!
            writer.writerow(row_data)


def clean_playlist_name(playlist_name):
    """
    Helper function to clean a `playlist_name` string for saving as a
    standardized CSV file name.
    """
    playlist_name = playlist_name.lower()
    playlist_name = playlist_name.replace(' ', '_')
    playlist_name = playlist_name.replace('.', '')
    playlist_name = playlist_name.replace(',', '_')
    playlist_name = playlist_name.replace('-', '_')
    playlist_name = playlist_name.replace('\'', '')
    playlist_name = playlist_name.replace('"', '')
    return playlist_name


def load_csv():
    """
    Loads data for the CSV
    """
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    sp = get_sp()
    playlist_data = sp.playlist(playlist_URI)
    playlist_name = clean_playlist_name(playlist_data['name'])

    filename = f'playlist_{playlist_name}.csv'
    csv_file = open(filename, "r")

    csv_reader = csv.DictReader(csv_file)

    tracks = []

    for row in csv_reader:
        row['popularity'] = int(row['popularity'])
        for feature in TARGET_FEATURES:
            if row[feature] is not None and row[feature] != '':
                row[feature] = float(row[feature])

        list_string = row['genres']
        contents = list_string[1:len(list_string) - 1]
        items = contents.split(", ")
        items_without_quote_marks = [item[1:len(item) - 1] for item in items]
        row['genres'] = items_without_quote_marks

        tracks.append(row)

    csv_file.close()
    return tracks  # A list of row dictionaries


def save_current_playlist_link():
    """
    Update playlist link based on the `playlist_link` value at the top
    of this program, saving it to the save_playlist_link.txt file (replacing
    the original contents).
    """
    file = open('save_playlist_link.txt', 'w')
    file.write(playlist_link)
    file.close()


def load_current_playlist_link():
    """
    Loads the contents of save_playlist_link.txt, returning
    the string.
    """
    file = open('save_playlist_link.txt', 'r')
    saved_playlist_link = file.readline()
    file.close()
    return saved_playlist_link


def load_tracks():
    """
    Loads track data with the playlist link specified in
    save_playlist_link.txt, saving the result data in a playlist CSV.
    """
    saved_playlist_link = load_current_playlist_link()
    # Update if the saved_playlist_link is changed.
    if saved_playlist_link != playlist_link:
        gen_csv()
        save_current_playlist_link()

    tracks = load_csv()
    return tracks


if __name__ == "__main__":
    load_tracks()
