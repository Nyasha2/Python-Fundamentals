from lab05_backend import load_processed_data, plot_nba_data
from lab05 import process_nba_finals_data

if __name__ == '__main__':
    process_nba_finals_data()
    made_x, made_y, missed_x, missed_y = \
        load_processed_data('processed_nba_data.csv', 'made')
    plot_nba_data(made_x, made_y, missed_x, missed_y)

