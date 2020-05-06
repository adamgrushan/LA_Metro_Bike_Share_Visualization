
""""
This file reads in bike share 2020 Q1 data and plots all the starting and
ending lats and longs of a specific day on a map using matplotlib.
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

    # determine min and maxes of start/end lat and start/end lon

    min_lon = min(df_lat_lon.start_lon.min(), df_lat_lon.end_lon.min())
    max_lon = max(df_lat_lon.start_lon.max(), df_lat_lon.end_lon.max())
    min_lat = min(df_lat_lon.start_lat.min(), df_lat_lon.end_lat.min())
    max_lat = max(df_lat_lon.start_lat.max(), df_lat_lon.end_lat.max())

    BBox = (min_lon, max_lon,
            min_lat, max_lat)

    print(BBox)

    # read in map file

    la_map = plt.imread('Data/LA_Map.png')

    # plot points

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.scatter(df_lat_lon.start_lon, df_lat_lon.start_lat, zorder=1, alpha=0.005, c='b', s=10)
    ax.set_title('Plotting Bike Locations on Los Angeles Map')
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    ax.imshow(la_map, zorder=0, extent=BBox, aspect='equal')

    plt.show()


