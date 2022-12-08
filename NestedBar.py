from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.transform import dodge
import json
Countries = ['China', 'Brazil', 'Thailand', 'Germany', 'Turkey']
deathData = ['New Deaths', 'Total Deaths', 'Deaths/Million']


# open json file
with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID = json.load(openfile)

Deaths = []
newDeaths = []
DeathMill = []
for rr in range(len(Countries)):
    Deaths.append(COVID.get(Countries[rr],{}).get('Deaths'))
    newDeaths.append(COVID.get(Countries[rr],{}).get('New Deaths'))
    DeathMill.append(COVID.get(Countries[rr],{}).get('Deaths/Million'))
data = {'Countries'         : Countries,
        'New Deaths'        : newDeaths,
        'Total Deaths'      : Deaths,
        'Deaths/Million'    : DeathMill}
print(data)

source = ColumnDataSource(data=data)

p = figure(x_range=Countries,  y_range=(0, 700000), title="COVID Death by Country",
           height=350, toolbar_location=None, tools="")

p.vbar(x=dodge('Countries', -0.25, range=p.x_range), top='New Deaths', source=source,
       width=0.2, color="#c9d9d3", legend_label="New Deaths")

p.vbar(x=dodge('Countries',  0.0,  range=p.x_range), top='Total Deaths', source=source,
       width=0.2, color="#718dbf", legend_label="Total Deaths")

p.vbar(x=dodge('Countries',  0.25, range=p.x_range), top='Deaths/Million', source=source,
       width=0.2, color="#e84d60", legend_label="Deaths/Million")

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)
