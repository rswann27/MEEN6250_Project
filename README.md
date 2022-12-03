# MEEN6250_Project
In this Python repo, we designed and implemented an interactive dashboard to support the visualization of coronavirus-related data. To accomplish this, we use Beautiful Soup for Data Scraping, Bokeh for displaying information, and Github for delivering the project.

'ScrapeWebsite.py' contains the function 'scrape_country' which takes two inputs: the desired country and a default arguement of a COVID data website url. The script is currently set up to scrape the following website:

https://www.worldometers.info/coronavirus/#nav-yesterday2

The function parses through all the counties' data and stores their Population, Total Deaths, Deaths Per Million, New Daily Deaths, and New Daily Deaths Per Million to a multi-dimensional dictionary sorted by country. The dictionary is then saved in a json file to the current folder location under 'COVID_*CurrentDate*.json'. If the desired country is found in the data set, the function will return that country's saved data to the termial, for example:

   Brazil :
   
    Daily Death Rate =  145
    
    Daily Death Rate Per Million =  0.067
    
    Cumulative Death Rate =  689998
    
    Cumulative Death Rate Per Million =  689998
    
If the country is not found in the data set, the funciton will return "Country not found". Whether or not the given country is found, the function will save all the countries' data to the json file.

To changed the desired country (it's currently set to 'Brazil') change the variable 'desiredCountry' on line 6 to your desired country and run the Python code.
 
See documentation for Beautiful Soup installation: 
https://www.crummy.com/software/BeautifulSoup/bs4/doc/



