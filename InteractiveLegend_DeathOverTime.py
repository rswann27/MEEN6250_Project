import pandas as pd
import numpy as np
import random
from bokeh.palettes import Turbo256
from bokeh.models import Legend
from bokeh.plotting import figure, show
from bokeh.models import TabPanel, Tabs
from bokeh.layouts import column, row

import json

# Import dictionary of country groups
from Country_Groups import countryGroups

# Country Groups for visualization from scraped keys and Country_Groups.py dictionary
africa = countryGroups.get("Africa")
asia = countryGroups.get("Asia")
oceania = countryGroups.get("Oceania")
europe = countryGroups.get("Europe")
south_america = countryGroups.get("South America")
north_america = countryGroups.get("North America")

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
    #   North America
    countryGroup.append('North America')
    groupDay.append(Days[rr])
    idx_SA = day.query("Countries == @north_america")
    groupDeathsPerMil.append(idx_SA['DeathsPerMil'].sum())
    groupDeaths.append(idx_SA['Deaths'].sum())
    groupNewDeaths.append(idx_SA['NewDeaths'].sum())
    groupNewDeathsPerMil.append(idx_SA['NewDeathsPerMil'].sum())
groupData = {   'Country Groups'    : countryGroup,
                'Day'               : groupDay,
                'Deaths'            : groupDeaths,
                'DeathsPerMil'      : groupDeathsPerMil,
                'NewDeaths'         : groupNewDeaths, 
                'NewDeathsPerMil'   : groupNewDeathsPerMil}
dfGroup = pd.DataFrame(groupData)

## TOTAL DEATHS
TOOLTIPS1 = [
    ("Deaths", "$y")
    ]
p1 = figure(width = 1200, height = 700, tooltips = TOOLTIPS1)
p1.add_layout(Legend(), 'right')
p1.title.text = 'Death in Continents over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = dfGroup[dfGroup['Country Groups'] == name]
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
p2.title.text = 'Death/Million in Continents over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = dfGroup[dfGroup['Country Groups'] == name]
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
p3.title.text = 'New Deaths in Continents over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = dfGroup[dfGroup['Country Groups'] == name]
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
p4.title.text = 'New Death/Million in Continents over Days in December\nSelect Country Group in Legend to hide'
for name, color in zip(countryGroup, my_pallete):
    country_df = dfGroup[dfGroup['Country Groups'] == name]
    p4.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

p4.legend.click_policy="hide"
p4.xaxis.axis_label = 'Dates in December'
p4.yaxis.axis_label = 'New Deaths Per Million'
tab4 = TabPanel(child = p4, title = 'New Deaths/Mil')

tabs = Tabs(tabs = [ tab1, tab2, tab3, tab4 ])

## Tab by Continent
subAfrica = df.query("Countries == @africa")
subAsia = df.query("Countries == @asia")
subOceania = df.query("Countries == @oceania")
subEurope = df.query("Countries == @europe")
subSA = df.query("Countries == @south_america")
subNA = df.query("Countries == @north_america")

## AFRICA
TOOLTIPSa = [
    ("New Death/Mil", "$y")
    ]
pa = figure(width = 1200, height = 700, tooltips = TOOLTIPSa)
pa.add_layout(Legend(), 'right')
pa.title.text = 'New Death/Million over Days in December\nSelect Country in Legend to hide'
for name, color in zip(africa, my_pallete):
    country_df = subAfrica[subAfrica['Countries'] == name]
    pa.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

pa.legend.click_policy="hide"
pa.xaxis.axis_label = 'Dates in December'
pa.yaxis.axis_label = 'New Deaths Per Million'
taba = TabPanel(child = pa, title = 'Africa')

## ASIA
TOOLTIPSb = [
    ("New Death/Mil", "$y")
    ]
pb = figure(width = 1200, height = 700, tooltips = TOOLTIPSb)
pb.add_layout(Legend(), 'right')
pb.title.text = 'New Death/Million over Days in December\nSelect Country in Legend to hide'
for name, color in zip(asia, my_pallete):
    country_df = subAsia[subAsia['Countries'] == name]
    pb.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

pb.legend.click_policy="hide"
pb.xaxis.axis_label = 'Dates in December'
pb.yaxis.axis_label = 'New Deaths Per Million'
tabb = TabPanel(child = pb, title = 'Asia')

## OCEANIA
TOOLTIPSc = [
    ("New Death/Mil", "$y")
    ]
pc = figure(width = 1200, height = 700, tooltips = TOOLTIPSc)
pc.add_layout(Legend(), 'right')
pc.title.text = 'New Death/Million over Days in December\nSelect Country in Legend to hide'
for name, color in zip(oceania, my_pallete):
    country_df = subOceania[subOceania['Countries'] == name]
    pc.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

pc.legend.click_policy="hide"
pc.xaxis.axis_label = 'Dates in December'
pc.yaxis.axis_label = 'New Deaths Per Million'
tabc = TabPanel(child = pc, title = 'Oceania')

## EUROPE
TOOLTIPSd = [
    ("New Death/Mil", "$y")
    ]
pd = figure(width = 1200, height = 700, tooltips = TOOLTIPSd)
pd.add_layout(Legend(), 'right')
pd.title.text = 'New Death/Million over Days in December\nSelect Country in Legend to hide'
for name, color in zip(europe, my_pallete):
    country_df = subEurope[subEurope['Countries'] == name]
    pd.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

pd.legend.click_policy="hide"
pd.xaxis.axis_label = 'Dates in December'
pd.yaxis.axis_label = 'New Deaths Per Million'
tabd = TabPanel(child = pd, title = 'Europe')

## SOUTH AMERICA
TOOLTIPSe = [
    ("New Death/Mil", "$y")
    ]
pe = figure(width = 1200, height = 700, tooltips = TOOLTIPSe)
pe.add_layout(Legend(), 'right')
pe.title.text = 'New Death/Million over Days in December\nSelect Country in Legend to hide'
for name, color in zip(south_america, my_pallete):
    country_df = subSA[subSA['Countries'] == name]
    pe.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

pe.legend.click_policy="hide"
pe.xaxis.axis_label = 'Dates in December'
pe.yaxis.axis_label = 'New Deaths Per Million'
tabe = TabPanel(child = pe, title = 'South America')

## NORTH AMERICA
TOOLTIPSf = [
    ("New Death/Mil", "$y")
    ]
pf = figure(width = 1200, height = 700, tooltips = TOOLTIPSf)
pf.add_layout(Legend(), 'right')
pf.title.text = 'New Death/Million over Days in December\nSelect Country in Legend to hide'
for name, color in zip(north_america, my_pallete):
    country_df = subNA[subNA['Countries'] == name]
    pf.line(x = country_df['Day'], y = country_df['NewDeathsPerMil'], color = color, legend_label=name)

pf.legend.click_policy="hide"
pf.xaxis.axis_label = 'Dates in December'
pf.yaxis.axis_label = 'New Deaths Per Million'
tabf = TabPanel(child = pf, title = 'North America')

tabs_Con = Tabs(tabs = [ taba, tabb, tabc, tabd, tabe, tabf ])

show(column(tabs,tabs_Con))
