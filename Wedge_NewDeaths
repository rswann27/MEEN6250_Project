from math import pi

import pandas as pd

from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.transform import dodge
import json

Countries = ['China', 'Brazil', 'Thailand', 'Germany', 'Turkey']
deathData = ['New Deaths', 'Total Deaths']


# open json file
with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID = json.load(openfile)

newDeaths = []
for rr in range(len(Countries)):
    newDeaths.append(COVID.get(Countries[rr],{}).get('New Deaths'))
data = {'Countries'         : Countries,
        'New Deaths'        : newDeaths}
print(data)


sum_deaths = sum(newDeaths)
print(sum_deaths)
angle = []

for rr in range(len(Countries)):
    angle.append(newDeaths[rr]/sum_deaths)
    
new_key = {}
for key in Countries:
    for value in newDeaths:
        new_key[key] = value
        newDeaths.remove(value)
        break

data = pd.Series(new_key).reset_index(name='value').rename(columns={'index': 'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(new_key)]
print(data)

p = figure(height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)
