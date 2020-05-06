
""""
This file reads in bike share 2020 Q1 data and plots all the starting and
ending lats and lons of the 2020 Q1 data on a map using matplotlib.
"""

# Imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # read in data

    df_all = pd.read_csv('Data/metro-bike-share-trips-2020-q1.csv')

    head = df_all.head()

    # return control totals

    row_count = len(df_all.index.to_list())
    print(row_count)

    # determine columns to use for lat and lon

    column_list = df_all.columns.to_list()
    for name in column_list:
        print(name)

    # clean data

    df_lat_lon = df_all[['start_lat', 'start_lon', 'end_lat', 'end_lon']]

    data_type_list = df_all.dtypes
    print(data_type_list)

    df_starts = df_lat_lon.iloc[:, 0:2]
    df_ends = df_lat_lon.iloc[:, 2:4]

    new_columns = ["lat", "lon"]
    df_starts.columns = new_columns
    df_ends.columns = new_columns

    df_stacked = pd.concat([df_starts, df_ends], ignore_index=True)

    # determine min and maxes of start/end lat and start/end lon

    min_lon = df_stacked.lon.min()
    max_lon = df_stacked.lon.max()
    min_lat = df_stacked.lat.min()
    max_lat = df_stacked.lat.max()

    BBox = (min_lon, max_lon,
            min_lat, max_lat)

    print(BBox)

    # read in map file

    la_map = plt.imread('Data/LA_Map.png')

    # plot all lats and lons

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.scatter(df_stacked.lon, df_stacked.lat, zorder=1, alpha=0.002, c='b', s=10)
    ax.set_title('Plotting Bike Locations on Los Angeles Map')
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    ax.imshow(la_map, zorder=0, extent=BBox, aspect='equal')

    plt.show()