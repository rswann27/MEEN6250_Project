from bs4 import BeautifulSoup
import requests
import json
from datetime import date

desiredCountry = 'Brazil'

def scrape_country(cntry,url ="https://www.worldometers.info/coronavirus/#nav-yesterday2"):
    bool = 1

    # CHECK for valid url
    if url != "https://www.worldometers.info/coronavirus/#nav-yesterday2" or url !="https://www.nytimes.com/interactive/2021/world/covid-cases.html":
        print("Not valid webset - setting to default")
        url ="https://www.worldometers.info/coronavirus/#nav-yesterday2"

    # SCRAPE web for data:
    result = requests.get(url).text
    doc = BeautifulSoup(result, 'html.parser')
    if url == "https://www.nytimes.com/interactive/2021/world/covid-cases.html":
        tbody = doc.find('tbody', attrs={'class':"children"})
        cities = tbody.find_all('tr')

        data = {}
        for i in range(len(cities)):
            tds = cities[i].find_all('td')

            name = tds[0].text
            name = name.replace('›', '')
            name = name.strip()

            ''''
            ## NEW CASES
            dailyCases = tds[1].text
            dailyCases = dailyCases.strip()
            dailyCases = int(dailyCases.replace(',', ''))
            data.setdefault(name, {})['Daily Case Rate'] = dailyCases

            # NEW CASES Per MILLION
            if tds[2].text == '—':
                dailyCaseperMil = 0.0
            else:
                dailyCaseperMil = tds[2].text
                dailyCaseperMil = dailyCaseperMil.strip()
            data.setdefault(name, {})['Daily Case Rate/Million'] = dailyCaseperMil
            '''

            # NEW DEATHS
            if tds[4].text == '—':
                newDeaths = 0.0
            else:
                newDeaths = tds[4].text
                newDeaths = newDeaths.strip()
                newDeaths = newDeaths.replace(',', '')
            data.setdefault(name, {})['New Deaths'] = newDeaths

            # NEW DEATHS Per MILLION
            if tds[5].text == '—':
                deathsPerMil = 0.0
            else:
                deathsPerMil = round(float(tds[5].text)/10, 2)
            data.setdefault(name, {})['New Deaths/Million'] = newDeaths

            # RETURN data associated with given country
            if cntry == name:
                print("\n\n\n",cntry,":" )
                '''
                print("   Daily Case Rate = ",data.get(cntry,{}).get('Daily Case Rate'))
                print("   Daily Case Rate Per Million = ",data.get(cntry,{}).get('Daily Case Rate/Million'))
                '''
                print("   Daily Death Rate = ", data.get(cntry,{}).get('New Deaths'))
                print("   Daily Death Rate Per Million = ", data.get(cntry,{}).get('New Deaths/Million'), "\n\n\n")
                # We found the given country
                bool = 0
            

    else: 
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
            deathPerMil = int(Deaths/population*1000000)
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
            data.setdefault(countries[i].text, {})['New Deaths/Million'] = round(newDeaths/population*100000,2)


            # RETURN data associated with given country
            if cntry == countries[i].text:
                print("\n\n\n",cntry,":" )
                print("   Daily Deaths = ", data.get(cntry,{}).get('New Deaths'))
                print("   Daily Death Rate Per Million = ", data.get(cntry,{}).get('New Deaths/Million'))
                print("   Cumulative Deaths = ", data.get(cntry,{}).get('Deaths'))
                print("   Cumulative Death Rate Per Million = ", data.get(cntry,{}).get('Deaths/Million'),"\n\n\n")
                # We found the given country
                bool = 0


    # Did we find the given country?
    if bool == 1:
        # No
        print('Country Not in Data Set')

    saveStr = "COVID_" + str(date.today()) + ".json"
    # SAVE Dictionary in JSON file
    print('Saving Data')
    with open(saveStr, "w") as outfile:
        json.dump(data, outfile)
           
#scrape_country(desiredCountry, "https://www.nytimes.com/interactive/2021/world/covid-cases.html")
scrape_country(desiredCountry)
#scrape_country(desiredCountry,"http://www.thisisnotvalid.com")
"""

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
seriousCritical = tds[9].text
casesPerMil = tds[10].text
deathsPerMil = tds[11].text
totalTests = tds[12].text
testsPerMil = tds[13].text
population = tds[14].text
print(deaths)
"""
