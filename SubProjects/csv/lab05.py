"""
CS 1 22fa
Lab 05 CSV Starter Code
Credit: Leo Jenkins
"""
import csv

COURT_LENGTH = 91.86
HIT_TYPES = ['single', 'double', 'triple', 'home_run']


def process_nba_finals_data():
    """
    Process nba data to extract shot coordinates and results (made/missed).
    Dataset used is 'nba_finals_data.csv' and results are saved
    to 'processed_nba_data.csv'.

    Returns:
        - None
    """
    # two CSVs, one to read from and one to write to
    read_file = open('nba_finals_data.csv', 'r')
    write_file = open('processed_nba_data.csv', 'w')

    csv_reader = csv.DictReader(read_file)
    # fieldnames are the columns of the new csv
    csv_writer = csv.DictWriter(write_file, fieldnames=['x', 'y', 'result'])

    # write the fieldnames
    csv_writer.writeheader()

    for row in csv_reader:
        # we want to ignore empty cells
        if row['converted_x'] != '' and row['converted_y'] != '':
            x = float(row['converted_x'])
            # we want all of the data to be on one half of the court
            if float(row['converted_y']) > COURT_LENGTH / 2:
                y = COURT_LENGTH - float(row['converted_y'])
            else:
                y = float(row['converted_y'])

            # fill in the data of each column for the current row
            write_row = {'x': x, 'y': y, 'result': row['result']}
            csv_writer.writerow(write_row)

    read_file.close()
    write_file.close()


def process_mlb_statcast_data():
    """
    Process mlb data to extract batted ball coordinates and their results
    (hit/out). Dataset used is '2021_mlb_statcast_data.csv' and results
    are saved to 'processed_mlb_data.csv'.

    Returns:
        - None
    """
    # two CSVs, one to read from and one to write to
    read_file = open('2021_mlb_statcast_data.csv', 'r')
    write_file = open('processed_mlb_data.csv', 'w')

    csv_reader = csv.DictReader(read_file)
    # fieldnames are the columns of the new csv
    csv_writer = csv.DictWriter(write_file, fieldnames=(['x', 'y', 'result']))

    # write the fieldnames
    csv_writer.writeheader()

    for row in csv_reader:
        # X means the ball was batted into play
        if row['type'] == 'X':
            # we only care about hits which occurred in Philadelphia or Houston
            if row['home_team'] == 'PHI' or row['home_team'] == 'HOU':
                # we want to ignore empty cells
                if row['hc_x'] != '' and row['hc_y'] != '':
                    # hc_x, hc_y are the coordinates of the batted ball
                    x = float(row['hc_x'])
                    # we need to flip y=0 from the top of the screen to the
                    # bottom of the screen
                    y = 250 - float(row['hc_y'])

                    # there are four types of hits
                    if row['events'] in HIT_TYPES:
                        result = 'hit'
                    # every batted ball which is not a hit is an out
                    # (regardless of whether the fielding team made an error)
                    else:
                        result = 'out'

                    # fill in the data of each column for the current row
                    write_row = {'x': x, 'y': y, 'result': result}
                    csv_writer.writerow(write_row)

    read_file.close()
    write_file.close()
