from bs4 import BeautifulSoup
import requests

url = "https://www.worldometers.info/coronavirus/#countries"
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')
body = doc.tbody
countries = body.find_all('a',attrs={'class':"mt_a"})

#Print first country in list
print(countries[0].text)
    
#Print its total deaths
tr=countries[0].parent.parent
tds=tr.find_all('td')
deaths = tds[4].text

print(deaths)
