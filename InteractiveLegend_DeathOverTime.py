import pandas as pd
import numpy as np
import random
from bokeh.palettes import Turbo256
from bokeh.models import Legend
from bokeh.plotting import figure, show
from bokeh.models import TabPanel, Tabs

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
DeathsPerMil = []
Deaths = []
NewDeaths = []
NewDeathsPerMil = []

# December 7
for rr in range(len(WorldWide)):
    Day.append(7)
    Country.append(WorldWide[rr])
    DeathsPerMil.append(COVID2.get(WorldWide[rr],{}).get('Deaths/Million'))
    Deaths.append(COVID2.get(WorldWide[rr],{}).get('Deaths'))
    NewDeaths.append(COVID2.get(WorldWide[rr],{}).get('New Deaths'))
    NewDeathsPerMil.append(COVID2.get(WorldWide[rr],{}).get('New Deaths/Million'))

# December 8
for rr in range(len(WorldWide)):
    Day.append(8)
    Country.append(WorldWide[rr])
    DeathsPerMil.append(COVID3.get(WorldWide[rr],{}).get('Deaths/Million'))
    Deaths.append(COVID3.get(WorldWide[rr],{}).get('Deaths'))
    NewDeaths.append(COVID3.get(WorldWide[rr],{}).get('New Deaths'))
    NewDeathsPerMil.append(COVID3.get(WorldWide[rr],{}).get('New Deaths/Million'))

# December 10
for rr in range(len(WorldWide)):
    Day.append(10)
    Country.append(WorldWide[rr])
    DeathsPerMil.append(COVID4.get(WorldWide[rr],{}).get('Deaths/Million'))
    Deaths.append(COVID4.get(WorldWide[rr],{}).get('Deaths'))
    NewDeaths.append(COVID4.get(WorldWide[rr],{}).get('New Deaths'))
    NewDeathsPerMil.append(COVID4.get(WorldWide[rr],{}).get('New Deaths/Million'))

# December 11
for rr in range(len(WorldWide)):
    Day.append(11)
    Country.append(WorldWide[rr])
    DeathsPerMil.append(COVID5.get(WorldWide[rr],{}).get('Deaths/Million'))
    Deaths.append(COVID5.get(WorldWide[rr],{}).get('Deaths'))
    NewDeaths.append(COVID5.get(WorldWide[rr],{}).get('New Deaths'))
    NewDeathsPerMil.append(COVID5.get(WorldWide[rr],{}).get('New Deaths/Million'))

data = {'Countries'         : Country,
        'Day'               : Day,
        'Deaths'            : Deaths,
        'DeathsPerMil'      : DeathsPerMil,
        'NewDeaths'         : NewDeaths, 
        'NewDeathsPerMil'   : NewDeathsPerMil}
groupDeaths = []
groupDeathsPerMil = []
groupNewDeaths = []
groupNewDeathsPerMil = []

countryGroup = []
groupDay = []

df = pd.DataFrame(data)
Days = [7, 8, 10, 11]

for rr in range(len(Days)):
    today = Days[rr]
    day = df.query("Day == @today")
    #   Africa
    countryGroup.append('Africa')
    groupDay.append(Days[rr])
    idx_Africa = day.query("Countries == @africa")
    groupDeaths.append(idx_Africa['Deaths'].sum())
    groupDeathsPerMil.append(idx_Africa['DeathsPerMil'].sum())
    groupNewDeaths.append(idx_Africa['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_Africa['NewDeathsPerMil'].sum())
    #   Asia
    countryGroup.append('Asia')
    groupDay.append(Days[rr])
    idx_Asia = day.query("Countries == @asia")
    groupDeathsPerMil.append(idx_Asia['DeathsPerMil'].sum())
    groupDeaths.append(idx_Asia['Deaths'].sum())
    groupNewDeaths.append(idx_Asia['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_Asia['NewDeathsPerMil'].sum())
    #   Oceania
    countryGroup.append('Oceania')
    groupDay.append(Days[rr])
    idx_Oceania = day.query("Countries == @oceania")
    groupDeathsPerMil.append(idx_Oceania['DeathsPerMil'].sum())
    groupDeaths.append(idx_Oceania['Deaths'].sum())
    groupNewDeaths.append(idx_Oceania['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_Oceania['NewDeathsPerMil'].sum())
    #   Europe
    countryGroup.append('Europe')
    groupDay.append(Days[rr])
    idx_Europe = day.query("Countries == @europe")
    groupDeathsPerMil.append(idx_Europe['DeathsPerMil'].sum())
    groupDeaths.append(idx_Europe['Deaths'].sum())
    groupNewDeaths.append(idx_Europe['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_Europe['NewDeathsPerMil'].sum())
    #   South America
    countryGroup.append('South America')
    groupDay.append(Days[rr])
    idx_SA = day.query("Countries == @south_america")
    groupDeathsPerMil.append(idx_SA['DeathsPerMil'].sum())
    groupDeaths.append(idx_SA['Deaths'].sum())
    groupNewDeaths.append(idx_SA['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_SA['NewDeathsPerMil'].sum())
    #   European Union
    countryGroup.append('EU')
    groupDay.append(Days[rr])
    idx_EU = day.query("Countries == @european_union")
    groupDeathsPerMil.append(idx_EU['DeathsPerMil'].sum())
    groupDeaths.append(idx_EU['Deaths'].sum())
    groupNewDeaths.append(idx_EU['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_EU['NewDeathsPerMil'].sum())
    #   Nato
    countryGroup.append('NATO')
    groupDay.append(Days[rr])
    idx_Nato = day.query("Countries == @nato")
    groupDeathsPerMil.append(idx_Nato['DeathsPerMil'].sum())
    groupDeaths.append(idx_Nato['Deaths'].sum())
    groupNewDeaths.append(idx_Nato['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_Nato['NewDeathsPerMil'].sum())
    #   OPEC
    countryGroup.append('OPEC')
    groupDay.append(Days[rr])
    idx_opec = day.query("Countries == @opec")
    groupDeathsPerMil.append(idx_opec['DeathsPerMil'].sum())
    groupDeaths.append(idx_opec['Deaths'].sum())
    groupNewDeaths.append(idx_opec['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_opec['NewDeathsPerMil'].sum())
    #   g10
    countryGroup.append('G10')
    groupDay.append(Days[rr])
    idx_g10 = day.query("Countries == @g10")
    groupDeathsPerMil.append(idx_g10['DeathsPerMil'].sum())
    groupDeaths.append(idx_g10['Deaths'].sum())
    groupNewDeaths.append(idx_g10['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_g10['NewDeathsPerMil'].sum())
    #   g20
    countryGroup.append('G20')
    groupDay.append(Days[rr])
    idx_g20 = day.query("Countries == @g20")
    groupDeathsPerMil.append(idx_g20['DeathsPerMil'].sum())
    groupDeaths.append(idx_g20['Deaths'].sum())
    groupNewDeaths.append(idx_g20['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_g20['NewDeathsPerMil'].sum())
groupData = {   'Country Groups'    : countryGroup,
                'Day'               : groupDay,
                'Deaths'            : groupDeaths,
                'DeathsPerMil'      : groupDeathsPerMil,
                'NewDeaths'         : groupNewDeaths, 
                'NewDeathsPerMil'   : groupNewDeathsPerMil}
df = df = pd.DataFrame(groupData)

## TOTAL DEATHS
TOOLTIPS1 = [
    ("Deaths", "$y")
    ]
p1 = figure(width = 1200, height = 700, tooltips = TOOLTIPS1)
p1.add_layout(Legend(), 'right')
p1.title.text = 'Death in Country Groups over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = df[df['Country Groups'] == name]
    p1.line(x = country_df['Day'], y = country_df['Deaths'], color = color, legend_label=name)

p1.legend.click_policy="hide"
p1.xaxis.axis_label = 'Dates in December'
p1.yaxis.axis_label = 'Total Deaths'
tab1 = TabPanel(child = p1, title = 'Total Deaths')

## Deaths Per Million
TOOLTIPS2 = [
    ("Death/Mil", "$y")
    ]
p2 = figure(width = 1200, height = 700, tooltips = TOOLTIPS2)
p2.add_layout(Legend(), 'right')
p2.title.text = 'Death/Million in Country Groups over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = df[df['Country Groups'] == name]
    p2.line(x = country_df['Day'], y = country_df['DeathsPerMil'], color = color, legend_label=name)

p2.legend.click_policy="hide"
p2.xaxis.axis_label = 'Dates in December'
p2.yaxis.axis_label = 'Deaths Per Million'
tab2 = TabPanel(child = p2, title = 'Deaths/Mil')

## New Deaths
TOOLTIPS3 = [
    ("New Deaths", "$y")
    ]
p3 = figure(width = 1200, height = 700, tooltips = TOOLTIPS3)
p3.add_layout(Legend(), 'right')
p3.title.text = 'New Deaths in Country Groups over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = df[df['Country Groups'] == name]
    p3.line(x = country_df['Day'], y = country_df['NewDeaths'], color = color, legend_label=name)

p3.legend.click_policy="hide"
p3.xaxis.axis_label = 'Dates in December'
p3.yaxis.axis_label = 'New Deaths'
tab3 = TabPanel(child = p3, title = 'New Deaths')

## New Deaths Per Million
TOOLTIPS4 = [
    ("New Deaths/Mil", "$y")
    ]
p4 = figure(width = 1200, height = 700, tooltips = TOOLTIPS4)
p4.add_layout(Legend(), 'right')
p4.title.text = 'New Death/Million in Country Groups over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = df[df['Country Groups'] == name]
    p4.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

p4.legend.click_policy="hide"
p4.xaxis.axis_label = 'Dates in December'
p4.yaxis.axis_label = 'New Deaths Per Million'
tab4 = TabPanel(child = p4, title = 'New Deaths/Mil')

tabs = Tabs(tabs = [ tab1, tab2, tab3, tab4 ])
show(tabs)
