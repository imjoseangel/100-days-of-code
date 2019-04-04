#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ML Walk-Through"""
# pylint: disable=R0916

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in data into a dataframe
data = pd.read_csv('data/Energy_and_Water_Data_Disclosure_for\
_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')

# Display top of dataframe
print(data.head())

# See the column data types and non-missing values
data.info()

# Replace all occurrences of Not Available with numpy not a number
data = data.replace({'Not Available': np.nan})

# Iterate through the columns
for col in list(data.columns):
    # Select columns that should be numeric
    if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col
            or 'kWh' in col or 'therms' in col or 'gal' in col
            or 'Score' in col):
        # Convert the data type to float
        data[col] = data[col].astype(float)

# Statistics for each column
print(data.describe())

# Missing Values (From https://stackoverflow.com/questions/26266362)
# Function to calculate missing values by column


def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(columns={
        0: 'Missing Values',
        1: '% of Total Values'
    })

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
            '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
          "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    # Return the dataframe with missing information
    return mis_val_table_ren_columns


missing_values = missing_values_table(data)

# Get the columns with > 50% missing
missing_df = missing_values_table(data)
print(missing_df)
missing_columns = list(missing_df[missing_df['% of Total Values'] > 50].index)
print('We will remove %d columns.' % len(missing_columns))

# Drop the columns
data = data.drop(columns=list(missing_columns))

# Rename the score
data = data.rename(columns={'ENERGY STAR Score': 'score'})

# Histogram of the Energy Star Score
plt.style.use('fivethirtyeight')
plt.hist(data['score'].dropna(), bins=100, edgecolor='k')
plt.xlabel('Score')
plt.ylabel('Number of Buildings')
plt.title('Energy Star Score Distribution')
plt.show()

# Histogram Plot of Site EUI
plt.hist(data['Site EUI (kBtu/ft²)'].dropna(), bins=20, edgecolor='black')
plt.xlabel('Site EUI')
plt.ylabel('Count')
plt.title('Site EUI Distribution')
plt.show()
