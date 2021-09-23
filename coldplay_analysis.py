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
import matplotlib.pyplot as plt 
# import statsmodels.formula.api as smf
# import statsmodels.api as sm

from tabulate import tabulate
# from statsmodels.stats.diagnostic import normal_ad

"""""""""""""""
FUNCTIONS
"""""""""""""""
def read_data(file):
    dataframe = pd.read_excel(file)
    return dataframe

def create_list(dataframe, column_name):
    new_df = dataframe[column_name].tolist()
    return new_df

def remove_duplicates(data):
    new_data = []
    for i in data:
        if i not in new_data:
            new_data.append(i)
    return new_data

def drop_cols(data, column_num):
    new_df = data.drop(data.columns[[column_num]], axis = 1)
    return new_df
    
"""""""""""""""
SEPARATE DATA
"""""""""""""""
os.chdir('/Users/umreenimam/Documents/Coding/data_analysis/music_analysis')
file = 'coldplay_tracks.xlsx'
coldplay_df = read_data(file)

# Get release dates and album names
release_dates = create_list(coldplay_df, 'release_date')
album_names = create_list(coldplay_df, 'album')

# Remove duplicate years and album names
res_dates = remove_duplicates(release_dates)
albums = remove_duplicates(album_names)

# Create dataframe with release dates and album names
album_dates = pd.DataFrame(res_dates)
album_dates['albums'] = albums

# Rename column of album_dates dataframe
album_dates.columns = ['release_date', 'album']

# Format date column
dates = pd.to_datetime(album_dates['release_date'])
formatted_dates = dates.dt.strftime('%m/%d/%y')
album_dates['release_dates'] = formatted_dates

# Drop original date column
album_dates = album_dates.drop('release_date', axis = 1)

# Export dataframe to csv
album_dates.to_excel('album_dates.xlsx')

# Print album_dates in table form 
headers = ['index', 'album', 'release_date']
album_table = tabulate(album_dates, headers = headers, tablefmt = 'fancy_grid')
print(album_table)

# Create album dataframes
parachutes = coldplay_df.iloc[0:10, :]
a_rush = coldplay_df.iloc[10:21, :]
x_y = coldplay_df.iloc[21:34, :]
viva_la_vida = coldplay_df.iloc[34:44, :]
prospekt_march = coldplay_df.iloc[44:62, :]
mylo_xyloto = coldplay_df.iloc[62:76, :]
ghost_stories = coldplay_df.iloc[76:85, :]
head_full = coldplay_df.iloc[85:96, :]
everyday_life = coldplay_df.iloc[96:100, :]

# Drop first column and reset index
coldplay_df = drop_cols(coldplay_df, 0)
parachutes = drop_cols(parachutes, 0)
a_rush = drop_cols(a_rush, 0)
x_y = drop_cols(x_y, 0)
viva_la_vida = drop_cols(viva_la_vida, 0)
prospekt_march = drop_cols(prospekt_march, 0)
mylo_xyloto = drop_cols(mylo_xyloto, 0)
ghost_stories = drop_cols(ghost_stories, 0)
head_full = drop_cols(head_full, 0)
everyday_life = drop_cols(everyday_life, 0)

parachutes = parachutes.reset_index(drop = True)
a_rush = a_rush.reset_index(drop = True)
x_y = x_y.reset_index(drop = True)
viva_la_vida = viva_la_vida.reset_index(drop = True)
prospekt_march = prospekt_march.reset_index(drop = True)
mylo_xyloto = mylo_xyloto.reset_index(drop = True)
ghost_stories = ghost_stories.reset_index(drop = True)
head_full = head_full.reset_index(drop = True)
everyday_life = everyday_life.reset_index(drop = True)

# Export all dataframes as csv files
parachutes.to_excel('parachutes.xlsx')
a_rush.to_excel('a_rush.xlsx')
x_y.to_excel('x_y.xlsx')
viva_la_vida.to_excel('viva_la_vida.xlsx')
prospekt_march.to_excel('prospekt_march.xlsx')
mylo_xyloto.to_excel('mylo_xyloto.xlsx')
ghost_stories.to_excel('ghost_stories.xlsx')
head_full.to_excel('head_full.xlsx')
everyday_life.to_excel('everyday_life.xlsx')

"""""""""""""""
Explore DataFrames
"""""""""""""""
# Get top 10 songs from Coldplay's released albums
top_ten = coldplay_df.nlargest(10, 'popularity')
top_ten = drop_cols(top_ten, 2)
top_ten = top_ten.reset_index(drop = True)
top_ten.to_excel('top_ten.xlsx')



