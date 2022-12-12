# MEEN6250_Project
This Python repo creates an interactive dashboard to support the visualization of coronavirus-related data. To accomplish this, the project requires Beautiful Soup for Data Scraping, Bokeh for data visualization, and Github for project delivery.

To install Beautiful Soup, run the following command:
    pip install beautifulsoup4
See documentation for Beautiful Soup installation: 
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/

To install Bokeh, run the following command:
    pip install bokeh
See documentation for Bokeh installation:
    https://docs.bokeh.org/en/latest/docs/first_steps/installation.html

'ScrapeWebsite.py' contains the function 'scrape_country' which takes two inputs: the desired country and a default arguement of a COVID data website url set to Wolrd-o-Meter. The script is currently set up to scrape the following websites:

https://www.worldometers.info/coronavirus/#nav-yesterday2
https://www.nytimes.com/interactive/2021/world/covid-cases.html

The function parses through all the counties' data and creates a multi-dimensional dictionary sorted by country and store the following if parsing through World-o-Meter: Population, Total Deaths, Deaths Per Million, New Daily Deaths, and New Daily Deaths Per Million and if parsing through NYTimes: New Daily Deaths, and New Daily Deaths Per Million. The dictionary is then saved in a json file to the current folder location under 'COVID_*CurrentDate*.json'. If the desired country is found in the data set, the function will return that country's saved data to the termial, for example:

   Brazil :
   
    Daily Deaths =  104
    
    Daily Death Rate Per Million =  0.48
    
    Cumulative Deaths =  690739
    
    Cumulative Death Rate Per Million =  3207
    
If the country is not found in the data set, the funciton will return "Country not found". Whether or not the given country is found, the function will save all the countries' data to the json file.

To change the desired country (it's currently set to 'Brazil'), change the variable 'desiredCountry' on line 6 to the desired country.
To toggle the desired url from World-o-Meter to NYTime, uncomment line 135 and comment out line 136.

'Country_Groups.py' contains a dictionary of country groups to use in data visualization. Current groups include geographic regions, economic and political unions, and others. The dictionary can be readily modified by adding a "key" as the name of the desired region and a [list] containing the names of the countries in the group. Country names added to lists must match those scraped by 'ScrapeWebsite.py' to use in data sets. For example, 'Democratic Republic of the Congo' is saved as 'DRC' and 'United Kingdom' is saved as 'UK'. Groups can be used to compare COVID data among group members or can be aggregated to compare between groups.

To launch the Data Visulaization GUI run the script, 'InteractiveGUI.py'. This script visualizes data obtained from the .json files which was scraped by 'ScrapeWebsite.py'. For data distinction, the palette Turbo256 is imported to provide enough colors to potentially represent every country in a worldwide analysis. For further distinction, the palette is randomized to guarantee that countries near each other in visualization will be distinct.

The first set of figures displayed by 'InteractiveGUI.py' are Pie Charts displaying country data for New and Total Deaths. These parameters are computed as a percentage of the group aggregate and plotted into two Bokeh wedge charts. An interactive hover tool is provided to allow a user to move around the wedge chart and display the country and data value represented in the wedge segment. 
Below is an example of the wedge charts:
<img width="1176" alt="Screenshot 2022-12-11 at 8 26 37 PM" src="https://user-images.githubusercontent.com/107783708/206954816-42cb9c95-c920-47de-8a7d-41030b45e26e.png">

The second set of figures, are time series plots showing data for continent regions through out days in December. Tabs at the top of the figure allow the user to select between different data types: Total Deaths, Deaths/Mil, New Deaths, and New Deaths/Mil. An interactive hover tool is provided to inform the user of exact values on the plot. An interactive legend allows the user to remove data from the plot by selecting the desired data set in the legend.
![image](https://user-images.githubusercontent.com/118580455/206959167-aca26adf-f81c-4dc7-a915-037c7bd73552.png)

The third and final set of figures, are time series plots showing New Deaths per Million for countries in given continent regions through out days in December. Tabs at the top of the figure allow the user to select between different continents: Africa, Asia, Oceania, Europe, South America, and North American. An interactive hover tool is provided to inform the user of exact values on the plot. An interactive legend allows the user to remove data from the plot by selecting the desired data set in the legend.
![image](https://user-images.githubusercontent.com/118580455/206959295-635c5ce6-5f40-4b77-b6a2-262e0fbeb667.png)



