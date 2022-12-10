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
 
See documentation for Beautiful Soup installation: 
https://www.crummy.com/software/BeautifulSoup/bs4/doc/



