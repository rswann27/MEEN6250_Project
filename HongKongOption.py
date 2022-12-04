from bs4 import BeautifulSoup
import requests
import json

def scrape_country(cntry,url):

    if cntry == 'Hong Kong':

        result = requests.get(url).text
        doc = BeautifulSoup(result, 'html.parser')

        tbody = doc.find('tbody', attrs={'class':"children"})
        trs = tbody.find_all('tr')
        
        tds = trs[1].find_all('td')
        
        name = tds[0].text
        print(name)
        newDeaths = tds[4].text
        print('New Daily Death Rate: ', newDeaths)
        deathsPerMil = round(float(tds[5].text)/10, 2)
        print("Deaths per million", deathsPerMil)
        
    
scrape_country('Hong Kong',"https://www.nytimes.com/interactive/2021/world/covid-cases.html")
