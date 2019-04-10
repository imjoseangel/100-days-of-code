#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bokeh Visualization Template

This template is a general outline for turning your data into a
visualization using Bokeh.
"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# Import reset_output (only needed once)
from bokeh.plotting import reset_output

# My x-y coordinate data
x = [1, 2, 1]
y = [1, 1, 2]

# Output the visualization directly in the notebook
output_file('first_glyphs.html', title='First Glyphs')

# Create a figure with no toolbar and axis ranges of [0,3]
fig = figure(
    title='My Coordinates',
    plot_height=300,
    plot_width=300,
    x_range=(0, 3),
    y_range=(0, 3),
    toolbar_location=None)

# Draw the coordinates as circles
fig.circle(x=x, y=y, color='green', size=10, alpha=0.5)

# Preview and save
show(fig)

# Use reset_output() between subsequent show() calls, as needed
reset_output()
