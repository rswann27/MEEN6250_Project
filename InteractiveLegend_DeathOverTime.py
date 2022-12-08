import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show

import json
Countries = ["China", "Brazil", "Thailand", "Germany", "Turkey"]

# open json file
with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID07 = json.load(openfile)

# open json file
with open("COVID_2022-12-02.json", 'r') as openfile:
    COVID02 = json.load(openfile)

# open json file
with open("COVID_2022-12-03.json", 'r') as openfile:
    COVID03 = json.load(openfile)

source = ColumnDataSource(data = dict(
    x = [2, 3, 7],
    China = [COVID02.get('China',{}).get('Deaths'), COVID03.get('China',{}).get('Deaths'),COVID07.get('China',{}).get('Deaths')],
    Brazil = [COVID02.get('Brazil',{}).get('Deaths'), COVID03.get('Brazil',{}).get('Deaths'),COVID07.get('Brazil',{}).get('Deaths')],
    Thailand = [COVID02.get('Thailand',{}).get('Deaths'), COVID03.get('Thailand',{}).get('Deaths'),COVID07.get('Thailand',{}).get('Deaths')],
    Germany = [COVID02.get('Germany',{}).get('Deaths'), COVID03.get('Germany',{}).get('Deaths'),COVID07.get('Germany',{}).get('Deaths')],
    Turkey = [COVID02.get('Turkey',{}).get('Deaths'), COVID03.get('Turkey',{}).get('Turkey'),COVID07.get('Turkey',{}).get('Deaths')]
))

list_of_colors = ['Red', 'Orange','Green', 'Blue', 'Purple', ]

p = figure(width=400, height=400)

p.vline_stack(Countries, x='x', source=source, color=list_of_colors, legend_label = Countries)
p.legend.location = "top_left"
p.legend.click_policy="hide"
p.title.text = 'Deaths in Countries over Days\nSelect Countries in Legend to hide'

p.xaxis.axis_label = 'Dates in December'

p.yaxis.axis_label = 'Deaths [people]'

show(p)
