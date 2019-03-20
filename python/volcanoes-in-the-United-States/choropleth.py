#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Building Web Maps using Folium"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import json
import pandas as pd
import folium

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Loading the json data as python dictionary
GEO_DATA = json.load(open(WORK_DIR + "/data/us-states.json"))
EMP_DATA = pd.read_csv(WORK_DIR + "/data/us-unemployment.csv")

# Create base map
MAP = folium.Map(location=[37.0902, -100.7129], zoom_start=4)

# Method to create Choropleth map, All parameters are mandatory
folium.Choropleth(
    geo_data=GEO_DATA,
    data=EMP_DATA,
    name='Unemployment Rate',
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)').add_to(MAP)

# e the map
MAP.save("choropleth.html")
