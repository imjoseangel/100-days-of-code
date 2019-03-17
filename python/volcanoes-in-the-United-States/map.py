#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Building Web Maps using Folium"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Loading the json data as python dictionary
DATA = pd.read_csv(WORK_DIR + "/data/Volcanoes_USA.txt")
LAT = DATA['LAT']
LON = DATA['LON']
ELEVATION = DATA['ELEV']


#Function to change colors
def color_change(elev):
    """Change Color depending on Mountain Elevation"""

    if elev < 1000:
        return 'green'
    if 1000 <= elev < 3000:
        return 'orange'
    return 'red'


#Create base map
MAP = folium.Map(
    location=[37.296933, -121.9574983],
    zoom_start=5,
    tiles="CartoDB dark_matter")

#Create Cluster
MARKER_CLUSTER = MarkerCluster().add_to(MAP)

#Plot Markers
for LAT, LON, ELEVATION in zip(LAT, LON, ELEVATION):
    folium.CircleMarker(
        location=[LAT, LON],
        radius=9,
        popup=str(ELEVATION) + " m",
        fill_color=color_change(ELEVATION),
        color="gray",
        fill_opacity=0.9).add_to(MARKER_CLUSTER)

#Save the map
MAP.save("map.html")
