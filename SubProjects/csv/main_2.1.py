from lab05_backend import load_processed_data, plot_mlb_data
from lab05 import process_mlb_statcast_data

if __name__ == '__main__':
    process_mlb_statcast_data()
    hit_x, hit_y, out_x, out_y = \
        load_processed_data('processed_mlb_data.csv', 'hit')
    plot_mlb_data(hit_x, hit_y, out_x, out_y)
