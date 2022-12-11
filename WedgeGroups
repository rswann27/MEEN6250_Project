from math import pi

import pandas as pd
import random
from Country_Groups import countryGroups
from bokeh.palettes import Turbo256
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.transform import dodge
from bokeh.layouts import row
import json

my_pallete = list(Turbo256)
random.shuffle(my_pallete)

# open json file
with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID = json.load(openfile)

# Country Groups for visualization from scraped keys and Country_Groups.py
worldwide = list(COVID.keys())
africa = countryGroups.get("Africa")
asia = countryGroups.get("Asia")
oceania = countryGroups.get("Oceania")
europe = countryGroups.get("Europe")
south_america = countryGroups.get("South America")
european_union = countryGroups.get("EU")
nato = countryGroups.get("NATO")
opec = countryGroups.get("OPEC")
g10 = countryGroups.get("G10")
g20 = countryGroups.get("G20")

# Choose from the above variables of groups or create a list of countries to compare
# Save as variable Countries
Countries = g20
deathData = ['New Deaths', 'Total Deaths']

newDeaths = []
totalDeaths = []

for rr in range(len(Countries)):
    newDeaths.append(COVID.get(Countries[rr],{}).get('New Deaths'))
    totalDeaths.append(COVID.get(Countries[rr],{}).get('Deaths'))

data = {'Countries'         : Countries,
        'New Deaths'        : newDeaths,
        'Total Deaths'      : totalDeaths}


sum_new_deaths = sum(newDeaths)
sum_total_deaths = sum(totalDeaths)
angle = []
angle2 = []

for rr in range(len(Countries)):
    angle.append(newDeaths[rr]/sum_new_deaths)
    angle2.append(totalDeaths[rr]/sum_total_deaths)
    
new_key = {}
for key in Countries:
    for value1 in newDeaths:
        new_key[key] = value1
        newDeaths.remove(value1)
        break

data = pd.Series(new_key).reset_index(name='value').rename(columns={'index': 'country'})
data['value2'] = totalDeaths
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['angle2'] = data['value2']/data['value2'].sum() * 2*pi
data['color'] = my_pallete[0:len(new_key)]

p = figure(height=350, title="New Deaths", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

q = figure(height=350, title="Total Deaths", toolbar_location=None,
           tools="hover", tooltips="@country: @value2", x_range=(-0.5, 1.0))

q.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle2', include_zero=True), end_angle=cumsum('angle2'),
        line_color="white", fill_color='color', legend_field='country', source=data)

q.axis.axis_label = None
q.axis.visible = False
q.grid.grid_line_color = None

show(row(p,q))
