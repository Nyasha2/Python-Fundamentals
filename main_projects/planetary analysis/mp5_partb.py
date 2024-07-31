"""
CS1 22fa MP5 Part B
Starter Code

Student Name: Nyasha Makaya
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Separating this to keep things clean; this function
# returns a dictionary of { col -> [row values]}
# to make it easier to work with for plotting.
from mp5_utils import collect_column_data

# Constants for plotting the single trajectory
# We use offset factors here to generalize the label positioning
# for large vs. small distances
X_LABEL_OFFSET = 700
Y_LABEL_OFFSET = 50

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2

# Exercise B.1.


def calculate_velocity(vi, launch_angle):
    '''
    Calculates vx and vy velocities of the rocket based
    on an initial velocity and a launch angle.

    Arguments:
        - vi: initial velocity
        - launch_angle: the angle at which the rocket is launched

    Returns:
        - (vx, vy): a tuple of floats repressenting the velocity vector
        of vx and vy
    '''

    angle = math.radians(launch_angle)
    vx = vi * math.cos(angle)
    vy = vi * math.sin(angle)
    return (vx, vy)


# Exercise B.2.
def calculate_position(dt, vi, launch_angle, gravity):
    '''
    Calculate the position of the rocket at time dt after the
    launch of the rocket.

    Arguments:
        - dt: the time elapsed since the launch of the rocket
        - vi: initial velocity of the rocket
        - launch_angle: the angle at which the rocket is launched
        - gravity: float value of the acceleration due to gravity

    Returns:
        - (x, y): the position tuple of the rocket at dt
    '''
    (X0, Y0) = (0, 0)
    vx, vy = calculate_velocity(vi, launch_angle)
    x = (vx * dt) + X0
    y = (vy * dt) + (0.5 * -gravity * math.pow(dt, 2)) + Y0
    return x, y


# Exercise B.3.
def flight_time(vi, launch_angle, gravity):
    '''
    Calculate the total time of flight of a rocket from launching to
    landing.

    Arguments:
        - vi: initial velocity of the rocket
        - launch_angle: the angle at which the rocket is launched
        - gravity: float value of the acceleration due to gravity

     Returns:
        - time: (a float) the total time of travel of the rocket
    '''
    vx, vy = calculate_velocity(vi, launch_angle)
    time = 2 * ((0 - vy) / (-1 * gravity))
    return time

# Exercise B.4.


def generate_rocket_positions(vi, launch_angle, gravity, tof):
    '''
    calculate the co-ordinates of the position of the rocket at 0.1
    time intervals after the launch, and returns then as two lists in
    a tuple.

    Arguments:
        - tof: the total time of flight of the rocket
        - vi: initial velocity of the rocket
        - launch_angle: the angle at which the rocket is launched
        - gravity: float value of the acceleration due to gravity

    Returns:
        - (xs, ys) a tuple of lists, xs is a list of x co-ordingates,
        ys is a list of y co-ordinates
    '''
    xs = []
    ys = []

    for i in np.arange(0, tof, 0.1):
        px, py = calculate_position(i, vi, launch_angle, gravity)
        xs.append(px)
        ys.append(py)

    # Handles the last coordinate case when y == 0.0 (rocket hits ground)
    if ys[-1] != 0.0:
        px, py = calculate_position(tof, vi, launch_angle, gravity)
        xs.append(px)
        ys.append(py)

    return (xs, ys)


# Exercise B.5.
def plot_trial_data(ax):
    """
    Processes trial data from trial_data.csv to compare launches
    on a single Axes `ax`.

    Plots points of interest on the `ax` for each trial with annotated
    labels for each point, sharing the corresponding line color.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    column_data = collect_column_data('trial_data.csv')
    trials = column_data['Trial']
    vis = column_data['Initial Velocity']
    launch_angles = column_data['Launch Angle (degrees)']
    gravities = column_data['Gravity']
    # Asserting an invariant pre-condition (should always be true,
    # independent of any user input). Don't use assert for error-handling.
    assert len(trials) == len(vis) == len(launch_angles) == len(gravities)

    trial_count = len(trials)

    for i in range(trial_count):
        launch_angle = int(launch_angles[i])
        gravity = int(gravities[i])
        vi = int(vis[i])
        trial_no = trials[i]
        tof = flight_time(vi, launch_angle, gravity)

        # Use generate_rocket_positions to generate positions
        # for this trial
        x, y = generate_rocket_positions(vi, launch_angle, gravity, tof)

        # calculate the highest point
        highest_point = calculate_position(tof / 2, vi, launch_angle, gravity)

        legend_label = f'Trial #{trial_no} ({tof:.1f}s)'
        lines = ax.plot(
            x,
            y,
            label=legend_label,
            markersize=MARKER_SIZE,
            linewidth=LINE_WIDTH)

        # Gets the line color of the plotted line (since only one line
        # was plotted above, lines should be a list of 1 Line2D object).
        # This makes it easier to color plot labels with the same color as
        # the corresponding trajectory line.
        line_color = lines[0].get_color()

        # Plot the highest point and final landing point with labels
        landing_point = calculate_position(tof, vi, launch_angle, gravity)
        plot_labels(highest_point, landing_point, line_color, ax)


# Provided
def plot_labels(highest_pt, landing_pt, line_color, ax):
    """
    Plots the points of interest on the `ax` with annotated labels
    for each point, sharing the passed `line_color`.

    Arguments:
        - highest_point (int/float, int/float): (x, y) of launch peak
        - landing_pt (int/float, int/float): (x, y) of landing point
        - line_color (str): line color for labels to share with a plotted line
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # Plot total distance marker/label
    (half_dist, max_y) = highest_pt
    (total_dist, last_y) = landing_pt

    # Plot max height marker/label
    max_height_label = f'{max_y:.0f}m'
    max_label_coords = (half_dist + X_LABEL_OFFSET,
                        max_y + Y_LABEL_OFFSET)

    # Make sure you can reason about what these next statements do
    ax.annotate(max_height_label, xy=highest_pt,
                xytext=max_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(half_dist, max_y, marker='D',
            color=line_color, markersize=MARKER_SIZE)

    # Plot the label marking the total distance traveled
    dist_label = f'{total_dist:.0f}m'
    dist_label_coords = (total_dist - X_LABEL_OFFSET,
                         Y_LABEL_OFFSET)

    ax.annotate(dist_label, xy=landing_pt,
                xytext=dist_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(total_dist, last_y, marker='*',
            color=line_color, markersize=MARKER_SIZE)


# Provided
def configure_plot(ax):
    """
    Configures the settings of the `ax` plot, including
    setting up the legend for the markers, defining the x and y
    axis bounds and labels, and the title of the plot.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # A bit of a hack, but add the marker symbols to the legend
    # without adding a legend item for each plotted marker
    # Note: 'k' is the shorthand for black ('b' is blue)
    ax.plot([], [], 'k*', label='Max Distance', markersize=MARKER_SIZE)
    ax.plot([], [], 'kD', label='Max Height', markersize=MARKER_SIZE)

    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.legend(loc='upper left')
    X_BOUND_OFFSET = 100
    Y_BOUND_OFFSET = 100
    xbounds = ax.get_xbound()
    ybounds = ax.get_ybound()
    ax.set_xlim(xbounds[0] - X_BOUND_OFFSET, xbounds[-1] + X_BOUND_OFFSET)
    ax.set_ylim(ybounds[0], ybounds[-1] + (Y_BOUND_OFFSET))

    ax.set_title('Bottle Rocket Launch Experiments')


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of launches based on trial_data.csv.
    """
    fig, ax = plt.subplots()
    plot_trial_data(ax)
    configure_plot(ax)
    fig.set_size_inches(12, 8)
    plt.show()


if __name__ == '__main__':
    start()
