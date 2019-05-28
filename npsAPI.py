import requests
import json

api_key = 'QzrkLi65rTSMTrFTiDGsmdAxWpIpxa72X6JrPEQN'

class NPS():

    def __init__(self, api_key: str):
        self._apiKey = api_key

    def parksByState(self, stateCode):
        r = requests.get('https://developer.nps.gov/api/v1/parks?stateCode=' + stateCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    def parksBySearch(self, q:str):
        r = requests.get('https://developer.nps.gov/api/v1/parks?q=' + q +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data


    def parkData(self, parkCode):
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode +
        '&fields=image&api_key=' + self._apiKey)
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
    
    def ifParkAlertsNotZero(self, parkCode) -> bool:
        if len(self.getParkAlerts(parkCode)) > 0:
            return True

    # Campgrounds------------------------------------
    def getParkCampgroundData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/campgrounds?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data
    
    def ifCampgroundNotZero(self, parkCode) -> bool:
        if len(self.getParkCampgroundData(parkCode)) > 0:
            return True
    #------------------------------------------------

    # Visitor Centers
    def getVisitorcentersData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/visitorcenters?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data
    
    def ifVisitorcentersNotZero(self, parkCode) -> bool:
        if len(self.getVisitorcentersData(parkCode)) > 0:
            return True
        
    # Articles 
    def getArticleData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/articles?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    def ifArticlesNotZero(self, parkCode) -> bool:
        if len(self.getArticleData(parkCode)) > 0:
            return True

    # News
    def getNewsData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/newsreleases?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data
    
    def ifNewsReleasesNotZero(self, parkCode) -> bool:
        if len(self.getNewsData(parkCode)) > 0:
            return True

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