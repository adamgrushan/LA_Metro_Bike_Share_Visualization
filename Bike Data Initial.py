# This file reads in bike share 2020 Q1 data and plots a column

# Import

import pandas as pd
import matplotlib.pyplot as plt

def series_statistics(data_series):
    # Max
    max = data_series.max()

    # Min
    min = data_series.min()

    # Median
    median = data_series.median()

    # Mean
    mean = data_series.mean()

    print('\nStatistics')
    print('------------')
    print('Max is ' + str(max) + ' minutes')
    print('Min is ' + str(min) + ' minute')
    print('Median is ' + str(median) + ' minutes')
    print('Mean is ' + str(mean) + ' minutes')

def plot_histogram(data_series, bin_list=None, auto_bin=True):
    fig, ax = plt.subplots()
    # Case of auto_bin
    auto_bin_size = 50
    if bin_list is None and auto_bin == True:
        ax.hist(data_series, bins=auto_bin_size)
    # Custom bins specified
    elif bin_list is not None:
        ax.hist(data_series, bins=bin_list)
    # else plot normally
    else:
        ax.hist(data_series)

    # Cosmetics
    ax.set_title(data_series.name, fontweight='bold')
    ax.set_xlabel('Minutes')
    ax.set_ylabel('Frequency')

    # Show plot
    plt.show()
    plt.close()

if __name__ == '__main__':
    # Read the csv into a data frame
    data_path = '../Data/metro-bike-share-trips-2020-q1.csv'
    q1_data = pd.read_csv(data_path, index_col=False)

    # #print out each of the data columns
    #
    # column_list = q1_data.columns.to_list()
    # for name in column_list:
    #     print(name)

    # Clean dataframe
    q1_data = q1_data[q1_data['duration']<=240]
    # Select a specific series to plot
    trip_duration = q1_data['duration']

    # Generate some descriptive statistics
    series_statistics(trip_duration)

    # Plot the distribution of trip duration to find outliers
    bin_list = []
    bin_space = 5
    i = 0

    while i <= trip_duration.max():
        bin_list.append(i)
        i += bin_space

    print(bin_list)
    plot_histogram(trip_duration, bin_list=bin_list)



