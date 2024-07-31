"""
Leo Jenkins
CS1 Grant Research
Lab 05 CSV Provided Backend

This backend uses students' lab05.py functions to plot visualizations
of sports data analysis!
"""

import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc, PathPatch
from matplotlib.path import Path


def draw_court():
    """
    Draw a basketball court with exact dimensions, scaled for
    a small plot drawing.

    Inspired by:
    http://savvastjortjoglou.com/nba-shot-sharts.html

    Returns:
        - None
    """
    COURT_WIDTH = 49.21
    COURT_LENGTH = 91.86
    COLOR = 'Black'
    LINE_WIDTH = 2

    # Hoop (a simple circle)
    # Syntax: Circle(center_coords, <options>)
    # This creates a circle horizontally centered in the court and near
    # the bottom (y=4.75)
    hoop = Circle((COURT_WIDTH / 2, 4.75), radius=0.75, linewidth=LINE_WIDTH,
                  color=COLOR, fill=False)

    # Backboard (a rectangle)
    # Syntax: Rectangle(anchor_pt, width, height, <options>)
    # This creates a line shifted slightly left from the court center,
    # near the bottom (y=5)
    backboard = Rectangle(((COURT_WIDTH / 2) - 3, 4), 6, 0,
                          linewidth=LINE_WIDTH, color=COLOR)

    # Paint
    outer_box = Rectangle(((COURT_WIDTH - 16) / 2, 0), 16, 19,
                          linewidth=LINE_WIDTH, color=COLOR, fill=False)

    # Inside paint
    inner_box = Rectangle(((COURT_WIDTH - 12) / 2, 0), 12, 19,
                          linewidth=LINE_WIDTH, color=COLOR, fill=False)

    # Create free throw top arc
    top_free_throw = Arc(((COURT_WIDTH / 2), 19), 12, 12,
                         theta1=0, theta2=180,
                         linewidth=LINE_WIDTH, color=COLOR, fill=False)

    # Create free throw bottom arc
    bottom_free_throw = Arc(((COURT_WIDTH / 2), 19), 12, 12,
                            theta1=180, theta2=0,
                            linewidth=LINE_WIDTH, color=COLOR,
                            linestyle='dashed')

    # Restricted Zone; an arc with 4ft radius from center of the hoop
    restricted = Arc((COURT_WIDTH / 2, 4.75), 8, 8, theta1=0, theta2=180,
                     linewidth=LINE_WIDTH, color=COLOR)

    # Three point line
    corner_three_a = Rectangle((3, 0), 0, 14, linewidth=LINE_WIDTH,
                               color=COLOR)

    corner_three_b = Rectangle((COURT_WIDTH - 3, 0), 0, 14,
                               linewidth=LINE_WIDTH, color=COLOR)

    # 3pt arc
    three_arc = Arc((COURT_WIDTH / 2, 4.75), 46.9, 46.9,
                    theta1=22.5, theta2=157.5, linewidth=LINE_WIDTH,
                    color=COLOR)

    # Center Court
    center_outer_arc = Arc((COURT_WIDTH / 2, COURT_LENGTH / 2), 12, 12,
                           theta1=180, theta2=0,
                           linewidth=LINE_WIDTH, color=COLOR)
    center_inner_arc = Arc((COURT_WIDTH / 2, COURT_LENGTH / 2), 4, 4,
                           theta1=180, theta2=0,
                           linewidth=LINE_WIDTH, color=COLOR)

    # baselines
    outer_lines = Rectangle((0, 0), COURT_WIDTH, COURT_LENGTH / 2,
                            linewidth=LINE_WIDTH, color=COLOR, fill=False)

    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc, outer_lines]

    # gca stands for "get current axes"
    ax = plt.gca()

    # Populate the plot
    for element in court_elements:
        ax.add_patch(element)

    # return ax


def plot_nba_data(made_x, made_y, missed_x, missed_y):
    """
    Process and render nba shot data as a scatterplot on top of the
    basketball court drawing.

    Arguments:
        - `made_x` (list)
        - `made_y` (list)
        - `missed_x` (list)
        - `missed_y` (list)

    Returns:
        - None
    """
    plt.figure(figsize=(10, 9.4))
    draw_court()
    plt.scatter(made_x, made_y, color='green', alpha=0.5)
    plt.scatter(missed_x, missed_y, color='red', alpha=0.5)
    plt.show()


def draw_field():
    """
    Draw a baseball field with approximate dimensions, scaled
    for a small drawing.

    Returns:
        - None
    """
    COLOR = 'Black'
    LINE_WIDTH = 1

    codes = []
    vertices = []

    # infield diamond
    codes = [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
    vertices = [(126, 42), (152, 68), (126, 94), (100, 68), (0, 0)]

    # right foul line
    codes += [Path.MOVETO] + [Path.LINETO]
    vertices += [(152, 68), (126 + 93.889, 42 + 93.889)]

    # left foul line
    codes += [Path.MOVETO] + [Path.LINETO]
    vertices += [(100, 68), (126 - 93.889, 42 + 93.889)]

    # outfield fence
    outfield_fence = Arc((126, 42 + 93.889), 2 * 93.889, 156,
                         angle=0, theta1=0, theta2=180,
                         linewidth=LINE_WIDTH, color=COLOR)

    outfield_grass = Arc((126, 40 + 24.717), 2 * 38.812, 2 * 38.812,
                         angle=0, theta1=20, theta2=160,
                         linewidth=LINE_WIDTH, color=COLOR)

    # mound
    mound = Arc((126, 40 + 24.717), 2 * 3.676955, 2 * 3.676955,
                angle=0, theta1=0, theta2=360,
                linewidth=LINE_WIDTH, color=COLOR)

    path = Path(vertices, codes)
    pathpatch = PathPatch(path, facecolor='none', edgecolor=COLOR)

    ax = plt.gca()

    ax.add_patch(pathpatch)
    ax.add_patch(outfield_fence)
    ax.add_patch(outfield_grass)
    ax.add_patch(mound)

    # return ax


def plot_mlb_data(safe_x, safe_y, out_x, out_y):
    """
    Plot the mlb hit data as a scatterplot on top of the field drawing.

    Arguments:
        - `safe_x` (list)
        - `safe_y` (list)
        - `out_x` (list)
        - `out_y` (list)
    """
    plt.figure(figsize=(9, 8))
    plt.title('Locations and Results of Batted Balls in HOU and PHI in 2021')
    draw_field()
    plt.scatter(safe_x, safe_y, color='green', alpha=0.5)
    plt.scatter(out_x, out_y, color='red', alpha=0.5)
    plt.show()


def load_processed_data(filename, outcome):
    """
    Load the processed data from filename.
    Note: `outcome` is the positive outcome in the data (i.e. 'made')

    Arguments:
        - `filename` (str) - CSV filename
        - `outcome` (str)

    Returns:
        - (tup) - tuple of four lists of `float` values, representing
                  (true xs, true ys, false xs, false ys)
    """
    data = open(filename, 'r')
    csv_reader = csv.DictReader(data)

    true_x = []
    true_y = []
    false_x = []
    false_y = []

    for row in csv_reader:
        if row['result'] == outcome:
            true_x.append(float(row['x']))
            true_y.append(float(row['y']))
        else:
            false_x.append(float(row['x']))
            false_y.append(float(row['y']))

    return true_x, true_y, false_x, false_y
