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
from bokeh.layouts import gridplot

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Read the csv files
player_stats = pd.read_csv(
    WORK_DIR + '/data/2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv(
    WORK_DIR + '/data/2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv(
    WORK_DIR + '/data/2017-18_standings.csv', parse_dates=['stDate'])

# Output to file
output_file(
    'east-west-top-2-gridplot.html', title='Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create views for each team
rockets_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name='teamAbbr', group='GS')])

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
    x_axis_label='Date',
    y_axis_label='Wins',
    toolbar_location=None)

west_fig = figure(
    x_axis_type='datetime',
    plot_height=300,
    x_axis_label='Date',
    y_axis_label='Wins',
    toolbar_location=None)

# Configure the figures for each conference
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

west_fig.step(
    'stDate',
    'gameWon',
    color='#CE1141',
    legend='Rockets',
    source=standings_cds,
    view=rockets_view)
west_fig.step(
    'stDate',
    'gameWon',
    color='#006BB6',
    legend='Warriors',
    source=standings_cds,
    view=warriors_view)

# Reduce the width of both figures
east_fig.plot_width = west_fig.plot_width = 300

# Edit the titles
east_fig.title.text = 'Eastern Conference'
west_fig.title.text = 'Western Conference'

# Plot the two visualizations with placeholders
east_west_gridplot = gridplot([[west_fig, None], [None, east_fig]],
                              toolbar_location='right')

# Plot the two visualizations in a horizontal configuration
show(east_west_gridplot)
