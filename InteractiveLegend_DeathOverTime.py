import pandas as pd
import random
from bokeh.palettes import Turbo256
from bokeh.models import Legend
from bokeh.plotting import figure, show

import json

# Randomize color palette so similar colors won't be assigned near each other
my_pallete = list(Turbo256)
random.shuffle(my_pallete)

# open json file
with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID2 = json.load(openfile)
with open("COVID_2022-12-08.json", 'r') as openfile:
    COVID3 = json.load(openfile)
with open("COVID_2022-12-10.json", 'r') as openfile:
    COVID4 = json.load(openfile)
with open("COVID_2022-12-11.json", 'r') as openfile:
    COVID5 = json.load(openfile)
Countries = list(COVID2.keys())

Day = []
Country = []
Deaths = []

# December 7
for rr in range(len(Countries)):
    Day.append(7)
    Country.append(Countries[rr])
    Deaths.append(COVID2.get(Countries[rr],{}).get('Deaths/Million'))

# December 8
for rr in range(len(Countries)):
    Day.append(8)
    Country.append(Countries[rr])
    Deaths.append(COVID3.get(Countries[rr],{}).get('Deaths/Million'))

# December 10
for rr in range(len(Countries)):
    Day.append(10)
    Country.append(Countries[rr])
    Deaths.append(COVID4.get(Countries[rr],{}).get('Deaths/Million'))

# December 11
for rr in range(len(Countries)):
    Day.append(11)
    Country.append(Countries[rr])
    Deaths.append(COVID5.get(Countries[rr],{}).get('Deaths/Million'))

data = {'Countries' : Country,
        'Day'       : Day,
        'Deaths'    : Deaths}

df = pd.DataFrame(data)
p = figure(width = 1200, height = 700)
p.add_layout(Legend(), 'right')
p.title.text = 'Deaths/Million in Countries over Days in December\nSelect Countries in Legend to hide'
for name, color in zip(Country, my_pallete):
    country_df = df[df['Countries'] == name]
    p.line(x = country_df['Day'], y = country_df['Deaths'], color = color, legend_label=name)

#p.legend.location = "top_left"
p.legend.click_policy="hide"
p.xaxis.axis_label = 'Dates in December'
p.yaxis.axis_label = 'Deaths [1/1 Mil people]'

show(p)
