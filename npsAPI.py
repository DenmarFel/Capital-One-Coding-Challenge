import requests
import json

api_key = 'QzrkLi65rTSMTrFTiDGsmdAxWpIpxa72X6JrPEQN'

class NPS():

    def __init__(self, api_key: str):
        self._apiKey = api_key

    def parksByState(self, stateCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/parks?stateCode=' + stateCode + '&fields=images' +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    def parksBySearch(self, q:str) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/parks?q=' + q + '&fields=images' +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    def parkData(self, parkCode):
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode +
        '&fields=images&api_key=' + self._apiKey)
        data = r.json()
        data = data['data'][0]
        return data

    # Alerts
    def getParkAlerts(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/alerts?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    # Campgrounds------------------------------------
    def getParkCampgroundData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/campgrounds?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data
    
    #------------------------------------------------

    # Visitor Centers
    def getVisitorcentersData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/visitorcenters?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

        
    # Articles 
    def getArticleData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/articles?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    # News
    def getNewsData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/newsreleases?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

webApp = NPS(api_key)
'''
for park in webApp.getParkCampgroundData('yose'):
    print(park['name'])

print(webApp.ifCampgroundNotZero('yose'))
'''
'''
for center in webApp.getVisitorcentersData('zion'):
    print(center['name'])
'''
'''
print(webApp.parksByState('ca')[-1]['images'][0]['url'])
'''
