from bs4 import BeautifulSoup
import requests
import json

url = "https://www.worldometers.info/coronavirus/#countries"
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')
body = doc.tbody
countries = body.find_all('a',attrs={'class':"mt_a"})

data = {}
for i in range(len(countries)):
    tr=countries[i].parent.parent
    tds=tr.find_all('td')

    # TOTAL DEATHS
    Deaths = tds[4].text
    Deaths = Deaths.strip()
    data.setdefault(countries[i].text, {})['Deaths'] = Deaths

    # DEATHS Per MILLION
    deathPerMil = tds[4].text
    deathPerMil = deathPerMil.strip()
    data.setdefault(countries[i].text, {})['Deaths/Million'] = deathPerMil

    # TOTAL CASES
    totalCases = tds[13].text
    totalCases = totalCases.strip()
    data.setdefault(countries[i].text, {})['Total Cases'] = totalCases

    # NEW CASES
    casePerMil = tds[10].text
    casePerMil = casePerMil.strip()
    data.setdefault(countries[i].text, {})['Caese/Mil'] = casePerMil

    # CASES Per MILLION
    newCases = tds[3].text
    newCases = newCases.strip()
    data.setdefault(countries[i].text, {})['New Cases'] = newCases


    # POPULATION
    population = tds[14].text
    population = population.strip()
    data.setdefault(countries[i].text, {})['Population'] = population

with open("COVID.json", "w") as outfile:
    json.dump(data, outfile)


"""

#Print its total deaths
tr=countries[0].parent.parent
tds=tr.find_all('td')
Deaths = tds[4].text
Deaths = Deaths.strip()
Deaths = float(Deaths.replace(',', ''))

# open json file
with open("USAdata.json", 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

# Parse through
totalCases = tds[2].text
newCases = tds[3].text
totalDeaths = tds[4].text
newDeaths = tds[5].text
totalRecovered = tds[6].text
newRecovered = tds[7].text
activeCases = tds[8].text
casesPerMil = tds[10].text
deathsPerMil = tds[11].text
totalTests = tds[12].text
testsPerMil = tds[13].text
population = tds[14].text
print(deaths)
"""
