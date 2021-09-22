#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:21:57 2021

@author: umreenimam
"""

"""""""""""""""
IMPORTING PACKAGES
"""""""""""""""
import os
import pandas as pd 
import seaborn as sns
import numpy as np

"""""""""""""""
ANALYZE DATA
"""""""""""""""
os.chdir('/Users/umreenimam/Documents/Coding/data_analysis/music_analysis')

def read_data(file):
    dataframe = pd.read_csv(file, sep = ',')
    return dataframe

file = 'coldplay_tracks.csv'
coldplay_df = read_data(file)

release_date = coldplay_df['release_date'].tolist()
album_names = coldplay_df['album'].tolist()
album_names = np.array(album_names)

# Remove duplicate years 
res_dates = []
for i in release_date:
    if i not in res_dates:
        res_dates.append(i)
        
# Get album names and release dates 
albums = []
for i in album_names:
    if i not in albums:
        albums.append(i)

album_dates = pd.DataFrame(res_dates)

album_dates['albums'] = albums
# print(album_dates)
