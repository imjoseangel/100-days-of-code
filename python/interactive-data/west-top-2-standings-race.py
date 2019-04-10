#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd

# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Read the csv files
player_stats = pd.read_csv(
    WORK_DIR + '/data/2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv(
    WORK_DIR + '/data/2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv(
    WORK_DIR + '/data/2017-18_standings.csv', parse_dates=['stDate'])

west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') |
                        (standings['teamAbbr'] == 'GS')].
              loc[:, ['stDate', 'teamAbbr', 'gameWon']].sort_values(
                  ['teamAbbr', 'stDate']))
print(west_top_2.head())

# Output to file
output_file(
    'west-top-2-standings-race.html',
    title='Western Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
west_cds = ColumnDataSource(west_top_2)

# Create views for each team
rockets_view = CDSView(
    source=west_cds,
    filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(
    source=west_cds, filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create and configure the figure
west_fig = figure(
    x_axis_type='datetime',
    plot_height=300,
    plot_width=600,
    title='Western Conference Top 2 Teams Wins Race, 2017-18',
    x_axis_label='Date',
    y_axis_label='Wins',
    toolbar_location=None)

# Render the race as step lines
west_fig.step(
    'stDate',
    'gameWon',
    source=west_cds,
    view=rockets_view,
    color='#CE1141',
    legend='Rockets')
west_fig.step(
    'stDate',
    'gameWon',
    source=west_cds,
    view=warriors_view,
    color='#006BB6',
    legend='Warriors')

# Move the legend to the upper left corner
west_fig.legend.location = 'top_left'

# Show the plot
show(west_fig)
