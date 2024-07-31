from lab06_backend import get_angels_data
from lab06 import plot_angels_projections

if __name__ == "__main__":
    games_played, games_won = get_angels_data()
    plot_angels_projections(games_played, games_won)
