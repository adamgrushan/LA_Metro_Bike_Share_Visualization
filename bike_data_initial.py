# Description: Initial file to read in LA bike data and plots a column
# Author: Jack O'Grady
# Date: 4/29/20
# Contact: jack.ogrady.23@gmail.com

# Imports
import pandas as pd
import matplotlib.pyplot as plt


def series_statistics(data_series):
    # Max
    max = data_series.max()

    #Min
    min = data_series.min()

    # Mean
    mean = data_series.mean()

    # Median
    median = data_series.median()

    print('\nStatistics')
    print('-----------')
    print('Max = ' + str(max) + ' min')
    print('Min = ' + str(min) + ' min')
    print('Mean = ' + str(mean) + ' min')
    print('Median = ' + str(median) + ' min')


def plot_histogram_from_series(data_series, bin_list=None, auto_bin=True):
    # Set up axes
    fig, ax = plt.subplots()

    # Create the histogram

    # Case of auto bin
    auto_bin_size = 50
    if bin_list is None and auto_bin == True:
        ax.hist(data_series, bins=auto_bin_size)
    # Custom bins specified
    elif bin_list is not None:
        ax.hist(data_series, bins=bin_list)
    # Else, plot normally
    else:
        ax.hist(data_series)

    # Cosmetics
    ax.set_title(data_series.name, fontweight='bold')
    ax.set_xlabel('Minutes')
    ax.set_ylabel('Frequency')

    plt.show()
    plt.close()


if __name__ == '__main__':
    # Read the csv into a dataframe

    # defining the location of the csv file
    data_path = '../data/metro-bike-share-trips-2020-q1.csv'
    # read the csv file into a dataframe
    q1_data = pd.read_csv(data_path, index_col=False)

    # # print out each of the data columns
    # column_list = q1_data.columns.to_list()
    # for name in column_list:
    #     print(name)

    # Select a specific series to plot

    # Getting the duration series
    # Clean dataframe
    q1_data = q1_data[q1_data['duration'] < 240]
    trip_durations = q1_data['duration']

    # Generate some statistics about this series
    series_statistics(trip_durations)

    # Plot a distribution of trip duration to find noise
    bin_list = []
    bin_space = 5
    i = 0
    while i <= trip_durations.max():
        bin_list.append(i)
        i += bin_space


    plot_histogram_from_series(trip_durations, bin_list=bin_list)
