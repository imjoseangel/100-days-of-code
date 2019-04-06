#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ML Walk-Through"""
# pylint: disable=R0916

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# Pandas and numpy for data manipulation
import pandas as pd
import numpy as np

# Seaborn for visualization
import seaborn as sns

# Matplotlib visualization
import matplotlib.pyplot as plt

# Internal ipython tool for setting figure size
from IPython.core.pylabtools import figsize

# No warnings about setting value on copy of slice
pd.options.mode.chained_assignment = None

# Display up to 60 columns of a dataframe
pd.set_option('display.max_columns', 60)

# Set default font size
plt.rcParams['font.size'] = 24

# Seaborn Font Size
sns.set(font_scale=2)

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

figsize(8, 8)

# Rename the score
data = data.rename(columns={'ENERGY STAR Score': 'score'})

# Histogram of the Energy Star Score
plt.style.use('fivethirtyeight')
plt.hist(data['score'].dropna(), bins=100, edgecolor='k')
plt.xlabel('Score')
plt.ylabel('Number of Buildings')
plt.title('Energy Star Score Distribution')
plt.show()

# Create a list of buildings with more than 100 measurements
types = data.dropna(subset=['score'])
types = types['Largest Property Use Type'].value_counts()
types = list(types[types.values > 100].index)

# Plot of distribution of scores for building categories
figsize(12, 10)

# Plot each building
for b_type in types:
    # Select the building type
    subset = data[data['Largest Property Use Type'] == b_type]

    # Density plot of Energy Star scores
    sns.kdeplot(subset['score'].dropna(), label=b_type, shade=False, alpha=0.8)

# label the plot
plt.xlabel('Energy Star Score', size=20)
plt.ylabel('Density', size=20)
plt.title('Density Plot of Energy Star Scores by Building Type', size=28)
plt.show()

# Create a list of boroughs with more than 100 observations
boroughs = data.dropna(subset=['score'])
boroughs = boroughs['Borough'].value_counts()
boroughs = list(boroughs[boroughs.values > 100].index)

# Plot of distribution of scores for boroughs
figsize(12, 10)

# Plot each borough distribution of scores
for borough in boroughs:
    # Select the building type
    subset = data[data['Borough'] == borough]

    # Density plot of Energy Star scores
    sns.kdeplot(subset['score'].dropna(), label=borough)

# label the plot
plt.xlabel('Energy Star Score', size=20)
plt.ylabel('Density', size=20)
plt.title('Density Plot of Energy Star Scores by Borough', size=28)
plt.show()

# Find all correlations and sort
correlations_data = data.corr()['score'].sort_values()

# Print the most negative correlations
print(correlations_data.head(15), '\n')

# Print the most positive correlations
print(correlations_data.tail(15))
