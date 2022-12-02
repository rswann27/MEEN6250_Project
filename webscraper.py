from bs4 import BeautifulSoup
import requests
import json

url = "https://www.worldometers.info/coronavirus/#nav-yesterday2"

def scrape_country(cntry,url):
    bool = 1

    # SCRAPE web for data:
    result = requests.get(url).text
    doc = BeautifulSoup(result, 'html.parser')
    tbody = doc.find('table', attrs={'id':"main_table_countries_yesterday2"}).tbody
    countries = tbody.find_all('a',attrs={'class':"mt_a"})

    # Organize Data for JSON file
    data = {}
    for i in range(len(countries)):
        tr=countries[i].parent.parent
        tds=tr.find_all('td')


        # POPULATION
        population = tds[14].text
        population = population.strip()
        population = int(population.replace(',', ''))
        data.setdefault(countries[i].text, {})['Population'] = population

        # TOTAL DEATHS
        Deaths = tds[4].text
        Deaths = Deaths.strip()
        if Deaths == "":
            Deaths = 0
        else:
            Deaths = int(Deaths.replace(',', ''))
        data.setdefault(countries[i].text, {})['Deaths'] = Deaths

        # DEATHS Per MILLION
        deathPerMil = tds[4].text
        deathPerMil = deathPerMil.strip()
        if deathPerMil == "":
            deathPerMil = 0
        else:
            deathPerMil = int(deathPerMil.replace(',', ''))
        data.setdefault(countries[i].text, {})['Deaths/Million'] = deathPerMil

        # NEW DEATHS
        newDeaths = tds[5].text
        newDeaths = newDeaths.strip()
        if newDeaths == "":
            newDeaths = 0
        else:
            newDeaths = int(newDeaths.replace(',', ''))
        data.setdefault(countries[i].text, {})['New Deaths'] = newDeaths

        # NEW DEATH per MILLION
        data.setdefault(countries[i].text, {})['New Deaths/Million'] = round(newDeaths/(population/100000),3)


        # RETURN data associated with given country
        if cntry == countries[i].text:
            print(cntry,":" )
            print("   Daily Death Rate = ", data.get(cntry,{}).get('New Deaths'))
            print("   Daily Death Rate Per Million = ", data.get(cntry,{}).get('New Deaths/Million'))
            print("   Cumulative Death Rate = ", data.get(cntry,{}).get('Deaths'))
            print("   Cumulative Death Rate Per Million = ", data.get(cntry,{}).get('Deaths/Million'))
            # We found the given country
            bool = 0

    # Did we find the given country?
    if bool == 1:
        # No
        print('Country Not in Data Set')

    # SAVE Dictionary in JSON file
    with open("COVID.json", "w") as outfile:
        json.dump(data, outfile)
"""
    # Return specific country
    for c in countries:
        if c.text == cntry:
            tds = c.parent.parent.find_all('td')
            deaths =tds[4].text
            deathsPerMil = tds[11].text
            newdeaths = int(tds[5].text)
            population = int(tds[14].text.replace(",",""))
            newDeathsPerMil = round(newdeaths/(population/100000),3)
            print(deaths)
            print(deathsPerMil)
            print((newdeaths))
            print(newDeathsPerMil)
"""            
scrape_country('Brazil',url)
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
