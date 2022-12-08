from bokeh.plotting import figure, show
from bokeh.models import LinearAxis, Range1d
import json

# open json file
with open("COVID_2022-12-07.json", 'r') as openfile:
    COVID = json.load(openfile)

Countries = ['China', 'Brazil', 'Thailand', 'Germany', 'Turkey']
colourss = ['Red', 'Orange','Green', 'Blue', 'Purple', ]
Deaths = []
pop = []
for rr in range(len(Countries)):
    Deaths.append(COVID.get(Countries[rr],{}).get('Deaths'))
    pop.append(COVID.get(Countries[rr],{}).get('Population'))
    

p = figure(width=400, height=400, title = "Deaths vs Population")

# add a circle renderer with a size, color, and alpha color="olive",
for rr in range(len(Countries)):
    p.star_dot(pop[rr], Deaths[rr], size=20,  alpha=0.5, color = colourss[rr], legend_label = Countries[rr])
p.yaxis.axis_label = "Total Deaths [people]"
p.xaxis.axis_label = "Population [people]"

# show the results
show(p)