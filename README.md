# MEEN6250_Project
In this Python repo, we designed and implemented an interactive dashboard to support the visualization of coronavirus-related data. To accomplish this, we use Beautiful Soup for Data Scraping, Bokeh for displaying information, and Github for delivering the project.

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

To change the desired country (it's currently set to 'Brazil') change the variable 'desiredCountry' on line 6 to the desired country.
To toggle the desired url from World-o-Meter to NYTime, uncomment line 135 and comment out line 136.

'Country_Groups.py' contains a dictionary of country groups to use in data visualization. Current groups include geographic regions, economic and political unions, and others. The dictionary can be readily modified by adding a "key" as the name of the desired region and a [list] containing the names of the countries in the group. Country names added to lists must match those scraped by 'ScrapeWebsite.py' to use in data sets. For example, 'Democratic Republic of the Congo' is saved as 'DRC' and 'United Kingdom' is saved as 'UK'. Groups can be used to compare COVID data among group members or can be aggregated to compare between groups.

'InteractiveLegend_DeathOverTime.py' visualizes data obtained from the .json files obtained from 'ScrapeWebsite.py'. Country data for New Deaths and Total deaths is computed as a percentage of the group aggregate and plotted into two Bokeh wedge charts. The palette Turbo256 is imported to provide enough colors to potentially represent every country in a worldwide analysis. The palette is also randomized so countries near each other in visualization will be distinct. An interactive hover tool is provided to allow a user to move around the wedge chart and display the country and data value represented in the wedge segment. 
Here is an example of the wedge charts:
<img width="1176" alt="Screenshot 2022-12-11 at 8 26 37 PM" src="https://user-images.githubusercontent.com/107783708/206954816-42cb9c95-c920-47de-8a7d-41030b45e26e.png">

'InteractiveLegend_DeathOverTime.py' comes with provided variables of groups imported from the 'Country_Groups.py' dictionary, such as 'europe', 'G20', and 'northAmerica'. A 'worldwide' variable is also taken from the .json keys and imported as a list of all countries in the data set if the user would like to plot worldwide data. 
 
See documentation for Beautiful Soup installation: 
https://www.crummy.com/software/BeautifulSoup/bs4/doc/



