from lab06_backend import get_bitcoin_data
from lab06 import plot_cherry_picked_bitcoin_data

if __name__ == '__main__':
    dates, prices = get_bitcoin_data()
    print(dates, prices)
    plot_cherry_picked_bitcoin_data(dates, prices)
