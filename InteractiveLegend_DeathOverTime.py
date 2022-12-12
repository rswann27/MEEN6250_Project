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

data = {'Countries' : Country,
        'Day'       : Day,
        'Deaths'    : Deaths}
groupDeaths = []
countryGroup = []
groupDay = []

df = pd.DataFrame(data)
Days = [7, 8, 10, 11]
# DAY 7 DATA
for rr in range(len(Days)):
    day = df.query("Day == 7")
    #   Africa
    countryGroup.append('Africa')
    groupDay.append(Days[rr])
    idx_Africa = day.query("Countries == @africa")
    groupDeaths.append(idx_Africa['Deaths'].sum())
    #   Asia
    countryGroup.append('Asia')
    groupDay.append(Days[rr])
    idx_Asia = day.query("Countries == @asia")
    groupDeaths.append(idx_Asia['Deaths'].sum())
    #   Oceania
    countryGroup.append('Oceania')
    groupDay.append(Days[rr])
    idx_Oceania = day.query("Countries == @oceania")
    groupDeaths.append(idx_Oceania['Deaths'].sum())
    #   Europe
    countryGroup.append('Europe')
    groupDay.append(Days[rr])
    idx_Europe = day.query("Countries == @europe")
    groupDeaths.append(idx_Europe['Deaths'].sum())
    #   South America
    countryGroup.append('South America')
    groupDay.append(Days[rr])
    idx_SA = day.query("Countries == @south_america")
    groupDeaths.append(idx_SA['Deaths'].sum())
    #   European Union
    countryGroup.append('EU')
    groupDay.append(Days[rr])
    idx_EU = day.query("Countries == @european_union")
    groupDeaths.append(idx_EU['Deaths'].sum())
    #   Nato
    countryGroup.append('NATO')
    groupDay.append(Days[rr])
    idx_Nato = day.query("Countries == @nato")
    groupDeaths.append(idx_Nato['Deaths'].sum())
    #   OPEC
    countryGroup.append('OPEC')
    groupDay.append(Days[rr])
    idx_opec = day.query("Countries == @opec")
    groupDeaths.append(idx_opec['Deaths'].sum())
    #   g10
    countryGroup.append('G10')
    groupDay.append(Days[rr])
    idx_g10 = day.query("Countries == @g10")
    groupDeaths.append(idx_g10['Deaths'].sum())
    #   g20
    countryGroup.append('G20')
    groupDay.append(Days[rr])
    idx_g20 = day.query("Countries == @g20")
    groupDeaths.append(idx_g20['Deaths'].sum())
groupData = {   'Country Groups'  : countryGroup,
                'Day'               : groupDay,
                'Deaths'            : groupDeaths}
df = df = pd.DataFrame(groupData)

TOOLTIPS = [
    ("Death/Mil", "$y")
    ]
p = figure(width = 1200, height = 700, tooltips = TOOLTIPS)
p.add_layout(Legend(), 'right')
p.title.text = 'Death/Million in Country Groups over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = df[df['Country Groups'] == name]
    p.line(x = country_df['Day'], y = country_df['Deaths'], color = color, legend_label=name)

#p.legend.location = "top_left"
p.legend.click_policy="hide"
p.xaxis.axis_label = 'Dates in December'
p.yaxis.axis_label = 'Deaths Per Million'

show(p)
