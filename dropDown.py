from bokeh.io import show
from bokeh.models import CustomJS, Dropdown
import json

file= open('COVID_2022-12-10.json')
data = json.load(file)
Countries =list(data)

metrics =list(data['China'].keys())[1:]

dropdown1 = Dropdown(label="Select Country", button_type="warning", menu=Countries)
dropdown1.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

dropdown2 = Dropdown(label="Select Another Country", button_type="warning", menu=Countries)
dropdown2.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))


Metrics_DropDown = Dropdown(label="Select Metric", button_type="warning", menu=metrics)
Metrics_DropDown.js_on_event("menu_item_click", CustomJS(code="console.log('Metrics_DropDown: ' + this.item, this.toString())"))

show(dropdown1)
