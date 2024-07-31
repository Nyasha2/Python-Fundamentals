import numpy as np
import matplotlib.pyplot as plt


# SECTION 1: Axis Manipulation
def plot_cherry_picked_bitcoin_data(date, price):
    """
    Plots bitcoin data from 2021-2022.

    Arguments:
        - date, price (both lists)

    Returns: 
        - None (plot pops up)
    """
    (fig, ax) = plt.subplots()

    # Plot the data
    ax.plot(date, price, color='black')
   
    # Title and labels
    ax.set_title('Daily Bitcoin Price (2021-2022)', fontsize=22)
    
    # 10 x ticks
    x_ticks = []
    for i in range(0, len(date), 100):
        x_ticks.append(date[i])

    # 100 y ticks
    y_ticks = []
    for price in range(10000, 100000, 10000):
        y_ticks.append(price)

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    # Restrict the x-axis
    ax.set_xlim('Jul 20, 2021', 'Oct 28, 2021')
    # Show the figure
    plt.show()


def plot_trimmed_y_axis_bar_graph(schools, laureates):
    """
    Plots the number of Nobel laureates per school.

    Arguments:
        - schools, laureates (both lists)
    
    Returns:
        - None (plot pops up)
    """
    # Create single Axes to manage the plotting
    (fig, ax) = plt.subplots()

    # Plot the data (bar chart)
    ax.bar(schools, laureates)

    # Title and labels
    ax.set_title('Nobel Prize winners', fontsize = 22)    
    ax.set_ylabel('Number of laureates')
    
    # Restrict the y-axis
    ax.set_ylim(33, 50)
    # Show the figure
    plt.show()


# SECTION 2: Spurious correlations
def plot_spurious_correlation(years, arcade_revenue, cs_doctorates):
    """
    Plots two statistics which are spuriously correlated.

    Arguments:
        - years, arcade_revenue, cs_doctorates (all lists)
    
    Returns:
        - None (plot pops up)
    """
    # Start the figure
    fig, ax1 = plt.subplots()

    # Allow for two functions on one plot
    ax2 = ax1.twinx()
    # Plot one in red and the other in black
    ax1.plot(years, arcade_revenue, color='red')
    ax2.plot(years, cs_doctorates, color='black')

    # Restrict the y-axes
    ax1.set_ylim([1, 2])
    ax2.set_ylim([500, 2000])

    # Title and labels
    # Title is wrapped
    plt.title('Total revenue generated by arcades correlates (98.51%) with ' +
              'computer science doctorates awarded in the US', wrap=True)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Arcade revenue (billions of USD)', color='red')
    ax2.set_ylabel('Computer science doctorates', color='black')

    # Show the figure
    plt.show()


# SECTION 3: Misleading trends
def plot_angels_projections(games, wins):
    """
    Plots two statistics which are spuriously correlated.

    Arguments:
        - games, wins (both lists)
    
    Returns:
        - None (plot pops up)
    """
    # Restrict the games and wins to the first 37 games
    early_games = games[:37]
    early_wins = wins[:37]
   
    # Find the line of best fit (ax + b)
    a, b = np.polyfit(early_games, early_wins, 1)
    extrapolation = []
    for x in range(101):
        extrapolation.append(a*x + b)

    # Create single Axes to manage the plotting
    (fig, ax) = plt.subplots()

    # Plot the data and the line of best fit
    ax.plot(games, extrapolation)
    ax.plot(games, wins)

    # Title and labels
    ax.set_title('LA Angel\'s Wins vs. Games played in the 2022 season')
    ax.set_xlabel('Games played')
    ax.set_ylabel('Games won')

    # Legend
    ax.legend(['Games they would have won', 'Games they won'])

    # Show the figure
    plt.show()
