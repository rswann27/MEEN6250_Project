from bokeh.plotting import figure
from bokeh import events
from bokeh.models import CustomJS, Div, Button
from bokeh.layouts import column, row
from bokeh.plotting import figure, show

import json

with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID = json.load(openfile)
Countries = list(COVID.keys())

TotalDeaths = []
Population = []
for rr in range(len(Countries)):
    TotalDeaths.append(COVID.get(Countries[rr],{}).get('Deaths'))
    Population.append(COVID.get(Countries[rr],{}).get('Population'))

p = figure(tools="box_select")
p.scatter(Population, TotalDeaths, radius=1, fill_alpha=0.6, line_color=None)

div = Div(width=400)
button = Button(label="Button", width=300)
layout = column(button, row(p, div))

# Events with no attributes
button.js_on_event(events.ButtonClick,  CustomJS(args=dict(div=div), code="""
div.text = "Button!";
""")) 

p.js_on_event(events.SelectionGeometry, CustomJS(args=dict(div=div), code="""
div.text = "Selection! <p> <p>" + JSON.stringify(cb_obj.geometry, undefined, 2);
"""))

show(layout)