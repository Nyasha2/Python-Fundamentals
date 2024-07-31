"""
CS 1 22fa 
Lab06 Provided Backend Code
Author: Leo Jenkins
"""
import csv

def get_angels_data():
    """
    Returns a (list, list) tuple of game numbers and wins,
    respectively, for the Angels in 2022. Data comes from
    angels_wins_2022.csv.

    Returns:
        - (list, list) tuple
    """
    csv_file = open('angels_wins_2022.csv', 'r')
    csv_reader = csv.DictReader(csv_file)

    xs = []
    ys = []

    wins = 0
    for row in csv_reader:
        xs.append(int(row['Gm#']))
        if row['W/L'] == 'W':
            wins += 1
        ys.append(wins)

    csv_file.close()
    return xs, ys
       

def get_bitcoin_data():
    """
    Returns a (list, list) tuple of dates and prices for
    Bitcoins collected from bitcoin_historical_data.csv.

    Returns:
        - (list, list) tuple
    """
    csv_file = open('bitcoin_historical_data.csv', 'r')
    csv_reader = csv.DictReader(csv_file)

    xs = []
    ys = []

    for row in csv_reader:
        xs.append(row['Date'])
        # Standardize price value (which may have ,) to float
        ys.append(float(row['Price'].replace(',', '')))

    csv_file.close()

    # Reverse the lists
    xs = xs[::-1]
    ys = ys[::-1]
    return xs, ys
