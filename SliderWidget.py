from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, output_file, show

import json

with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID = json.load(openfile)
Countries = list(COVID.keys())

TotalDeaths = []
Population = []
for rr in range(len(Countries)):
    TotalDeaths.append(COVID.get(Countries[rr],{}).get('Deaths'))
    Population.append(COVID.get(Countries[rr],{}).get('Population'))
#print(TotalDeaths[0:10])

y = TotalDeaths
source = ColumnDataSource(data=dict(x=Population, y=TotalDeaths))

# Plot
plot = figure(width=700, height=600)
plot.scatter('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
    const data = source.data;
    const f = cb_obj.value
    const x = data['x']
    const y = data['y']
    iter = 0
    for (let i = 0; i < x.length; i++) {
        if x[ii] < f{
            y[iter] = y[i]
            x[iter] = x[i]
            iter = iter + 1
        }
    }
    source.change.emit();
""")

slider = Slider(start=0, end=800000, value=10000, step=10000, title="TotalDeaths")

slider.js_on_change('value', callback)
layout = column(slider, plot)

plot.yaxis.axis_label = "Total Deaths [people]"
plot.xaxis.axis_label = "Population [people]"


show(layout)
