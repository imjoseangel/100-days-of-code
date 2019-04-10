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
    'east-top-2-standings-race.html',
    title='Eastern Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create views for each team
celtics_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name='teamAbbr', group='BOS')])
raptors_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name='teamAbbr', group='TOR')])

# Create and configure the figure
east_fig = figure(
    x_axis_type='datetime',
    plot_height=300,
    plot_width=600,
    title='Eastern Conference Top 2 Teams Wins Race, 2017-18',
    x_axis_label='Date',
    y_axis_label='Wins',
    toolbar_location=None)

# Render the race as step lines
east_fig.step(
    'stDate',
    'gameWon',
    color='#007A33',
    legend='Celtics',
    source=standings_cds,
    view=celtics_view)
east_fig.step(
    'stDate',
    'gameWon',
    color='#CE1141',
    legend='Raptors',
    source=standings_cds,
    view=raptors_view)

# Move the legend to the upper left corner
east_fig.legend.location = 'top_left'

# Show the plot
show(east_fig)
