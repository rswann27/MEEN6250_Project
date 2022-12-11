import pandas as pd
import numpy as np
import random
from bokeh.palettes import Turbo256
from bokeh.models import Legend
from bokeh.plotting import figure, show

import json

# Import dictionary of country groups
from Country_Groups import countryGroups

# Country Groups for visualization from scraped keys and Country_Groups.py dictionary
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
WorldWide = list(COVID2.keys())

Day = []
Country = []
Deaths = []

# December 7
for rr in range(len(WorldWide)):
    Day.append(7)
    Country.append(WorldWide[rr])
    Deaths.append(COVID2.get(WorldWide[rr],{}).get('Deaths/Million'))

# December 8
for rr in range(len(WorldWide)):
    Day.append(8)
    Country.append(WorldWide[rr])
    Deaths.append(COVID3.get(WorldWide[rr],{}).get('Deaths/Million'))

# December 10
for rr in range(len(WorldWide)):
    Day.append(10)
    Country.append(WorldWide[rr])
    Deaths.append(COVID4.get(WorldWide[rr],{}).get('Deaths/Million'))

# December 11
for rr in range(len(WorldWide)):
    Day.append(11)
    Country.append(WorldWide[rr])
    Deaths.append(COVID5.get(WorldWide[rr],{}).get('Deaths/Million'))

# Initialize New Data Set
africaDeaths = []
asiaDeaths = []
oceaniaDeaths = []
europeDeaths = []
saDeaths = []
euDeaths = []
natoDeaths = []
opecDeaths = []
g10Deaths = []
g20Deaths = []

data = {'Countries' : Country,
        'Day'       : Day,
        'Deaths'    : Deaths}

df = pd.DataFrame(data)
Days = [7, 8, 10, 11]
# DAY 7 DATA
for rr in range(len(Days)):
    day = df.query("Day == 7")
    #   Africa
    idx_Africa = day.query("Countries == @africa")
    africaDeaths.append(idx_Africa['Deaths'].sum())
    #   Asia
    idx_Asia = day.query("Countries == @asia")
    asiaDeaths.append(idx_Asia['Deaths'].sum())
    #   Oceania
    idx_Oceania = day.query("Countries == @oceania")
    oceaniaDeaths.append(idx_Oceania['Deaths'].sum())
    #   Europe
    idx_Europe = day.query("Countries == @europe")
    europeDeaths.append(idx_Europe['Deaths'].sum())
    #   South America
    idx_SA = day.query("Countries == @south_america")
    saDeaths.append(idx_SA['Deaths'].sum())
    #   Eurpopean Union
    idx_EU = day.query("Countries == @european_union")
    euDeaths.append(idx_EU['Deaths'].sum())
    #   Nato
    idx_Nato = day.query("Countries == @nato")
    natoDeaths.append(idx_Nato['Deaths'].sum())
    #   OPEC
    idx_opec = day.query("Countries == @opec")
    opecDeaths.append(idx_opec['Deaths'].sum())
    #   g10
    idx_g10 = day.query("Countries == @g10")
    g10Deaths.append(idx_g10['Deaths'].sum())
    #   g20
    idx_g20 = day.query("Countries == @g20")
    g20Deaths.append(idx_g20['Deaths'].sum())
print(g20Deaths)
'''
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
'''