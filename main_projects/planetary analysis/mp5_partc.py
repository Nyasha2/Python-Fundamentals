"""
CS1 22fa MP5 Part C

Student Name: Nyasha Makaya

Brief Overview: This program takes a csv files with information about
planets and plot a graph depicting the volumes of each graph

Data Source(s): planets.csv
Data Science Question: What are the approximate volumes of the planets
in our solar system.

Room for Improvement: (Optional)
"""

import matplotlib.pyplot as plt
import csv
# You may add additional imports if you choose to use them

# You may choose to change/add constants here as appropriate for
# your plotting program.

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2
PI = 3.14


def calculate_volume(diameter):
    volume = 4 / 3 * PI * pow(diameter / 2, 3)
    return volume


def plot_graph(ax):
    with open('planets.csv', 'r') as planets:
        csv_reader = csv.DictReader(planets)
        volumes = []
        planets = []
        for element in csv_reader:
            volume = calculate_volume(float(element['Diameter']))
            planet_name = (element['Name'])
            volumes.append(volume)
            planets.append(planet_name)

        ax.bar(planets, volumes)
        ax.set_title('Planet Volumes', fontsize=24)
        ax.set_ylabel('volume')


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of (TODO, finish this docstring).
    """
    # Provided as a start for Part C, modify as needed
    fig, ax = plt.subplots()
    plot_graph(ax)
    fig.set_size_inches(8, 8)
    plt.show()

    # Recommended: But you would need to change based on your
    # plot programming. Remove if you don't use this.
    # configure_plot(ax)


if __name__ == '__main__':
    start()
