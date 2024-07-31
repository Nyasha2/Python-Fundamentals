"""
CS1 22fa MP5 Part A
Starter Code

Student Name: Nyasha Makaya
"""
import numpy as np
import matplotlib.pyplot as plt
import math

GRAVITY = 9.81          # m/s^2
ANGLE_OF_LAUNCH = 45    # in degrees from horizon
INITIAL_VELOCITY = 150  # m/s

# Constants for plotting the single trajectory
# Note: We could use offset factors (e.g. 5%) here to generalize the
# label positioning large vs. small distances, but to make it easier
# to test without floating point subtleties, we will use constants
X_LABEL_OFFSET = 150
Y_LABEL_OFFSET = 10

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2


# Exercise A.1.
def calculate_velocity():
    '''
    Calculates vx and vy velocities of the rocket based
    on an initial velocity and a launch angle.

    Arguments:
        - None

    Returns:
        - (vx, vy): a tuple of floats repressenting the velocity vector
        of vx and vy
    '''

    angle = math.radians(ANGLE_OF_LAUNCH)
    vx = INITIAL_VELOCITY * math.cos(angle)
    vy = INITIAL_VELOCITY * math.sin(angle)

    return (vx, vy)


# Exercise A.2.
def calculate_position(dt):
    '''
    Calculate the position of the rocket at time dt after the
    launch of the rocket.

    Arguments:
        - dt: the time elapsed since the launch of the rocket

    Returns:
        - (x, y): the position tuple of the rocket at dt
    '''

    (X0, Y0) = (0, 0)
    starting_speeds = calculate_velocity()
    vx = starting_speeds[0]
    vy = starting_speeds[1]
    x = (vx * dt) + X0
    y = (vy * dt) + (0.5 * -GRAVITY * math.pow(dt, 2)) + Y0

    return x, y


# Exercise A.3.
def flight_time():
    '''
    Calculate the total time of flight of a rocket from launching to
    landing.

    Arguments:
        - None

     Returns:
        - time: (a float) the total time of travel of the rocket
    '''
    vx, vy = calculate_velocity()

    time = 2 * ((0 - vy) / (-1 * GRAVITY))
    return time


# Exercise A.4.
def generate_rocket_positions(tof):
    '''
    calculate the co-ordinates of the position of the rocket at 0.1
    time intervals after the launch, and returns then as two lists in
    a tuple.

    Arguments:
        - tof: the total time of flight of the rocket

    Returns:
        - (xs, ys) a tuple of lists, xs is a list of x co-ordingates,
        ys is a list of y co-ordinates
    '''
    xs = []
    ys = []
    for i in np.arange(0, tof, 0.1):
        px, py = calculate_position(i)
        xs.append(px)
        ys.append(py)

    # Handles the last coordinate case when y == 0.0 (rocket hits ground)
    if ys[-1] != 0.0:
        px, py = calculate_position(tof)
        xs.append(px)
        ys.append(py)
    return (xs, ys)


# Exercise: A.5.
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

    (half_dist, max_y) = highest_pt
    # (2293.577981651376, 0.0)
    (total_dist, last_y) = landing_pt
    # Plot max height marker/label

    # Maxh_label: '573m'
    maxh_label = f'{max_y:.0f}m'

    # (1296.788990825688, 583.3944954128439)
    maxh_label_coords = (half_dist + X_LABEL_OFFSET,
                         max_y + Y_LABEL_OFFSET)

    # Make sure you can reason about what these next statements do
    ax.annotate(maxh_label, xy=highest_pt, xytext=maxh_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(half_dist, max_y, marker='D', color=line_color,
            markersize=MARKER_SIZE)

    # Next, we plot the label marking the total distance traveled
    # (when the rocket lands)

    # dist_label: '2294m'
    dist_label = f'{total_dist:.0f}m'
    # dist_label_coords : '(2143.577981651376, 10)'
    dist_label_coords = (total_dist - X_LABEL_OFFSET,
                         Y_LABEL_OFFSET)

    ax.annotate(dist_label, xy=landing_pt, xytext=dist_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(total_dist, last_y, marker='*', color=line_color,
            markersize=MARKER_SIZE)


def plot_launch(ax):
    """
    Plots the launch data on the provided `ax`, creating a trajectory
    line graph with two plotted points of interest (max height and total
    distance traveled). Also sets up the legend for the plot, including
    the trajectory line and markers for the max height and landing points.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # Generate the x/y values for the line
    tof = flight_time()
    (xs, ys) = generate_rocket_positions(tof)

    # The highest point is exactly mid-launch
    highest_pt = calculate_position(tof / 2)

    # The rocket lands at the last (x, y) position
    landing_pt = (xs[-1], ys[-1])

    legend_label = f'Launch Trajectory ({tof:.1f}s)'

    # Plot the launch trajectory line using a color and line
    # style of choice (the shown graph uses a solid green line).
    # Use ax.plot to specify the appropriate keywords to set
    # LINE_WIDTH and MARKER_SIZE. Set the label of the plotted line
    # to be legend_label. Hint: our solution has 3 arguments (including
    # a shorthand formatter string) followed by 3 keyword arguments.

    lines = ax.plot(
        xs,
        ys,
        color='green',
        linewidth=LINE_WIDTH,
        markersize=MARKER_SIZE,
        label=legend_label)  # I honestly do not know what we are doing

    # The rest of the code below should be unmodified

    # Get the line color of the plotted line (lines is a list
    # of all lines plotted above, but we only have one)
    line_color = lines[0].get_color()

    # # Pass the two points of interest to plot the labelled
    # # points sharing the same line color as the line,
    # # and passing the required Axes which contains state
    # # and methods for the plot we've been modifying
    plot_labels(highest_pt, landing_pt, line_color, ax)


# Provided
def configure_plot(ax):
    """
    Configures the settings of the `ax` plot, including
    setting up the legend for the markers, defining the x and y
    axis bounds and labels, and the title of the plot.
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

    ax.set_title('Bottle Rocket Launch: Trajectory on Earth')


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of the test launch data using this
    program's constants for an example initial velocity, angle, and gravity
    rate.
    """
    fig, ax = plt.subplots()
    plot_launch(ax)
    configure_plot(ax)
    fig.set_size_inches(8, 8)
    plt.show()


if __name__ == '__main__':
    start()
