import requests
import json

api_key = 'QzrkLi65rTSMTrFTiDGsmdAxWpIpxa72X6JrPEQN'

class NPS():

    def __init__(self, api_key: str):
        self._apiKey = api_key

    def getStandardHours(self, parkCode):
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode + 
        '&fields=operatingHours&api_key=' + self._apiKey)
        data = r.json()
        items = data['data']
        items = items[0]
        result = items['operatingHours']
        result = result[0]
        print(result['standardHours'])

    def listParksByState(self, stateCode):
        r = requests.get('https://developer.nps.gov/api/v1/parks?stateCode=' + stateCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        result = []
        for park in data['data']:
            result.append(park['fullName'])
        return result

    def parkCodesByState(self, stateCode):
        r = requests.get('https://developer.nps.gov/api/v1/parks?stateCode=' + stateCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        result = []
        for park in data['data']:
            result.append(park['parkCode'])
        return result

    def parkDescription(self, parkCode):
        '''Returns description of park'''
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        data = data[0]
        result = data['description']
        return result
    
    def parkName(self, parkCode) -> str:
        '''Returns description of park'''
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        data = data[0]
        result = data['name']
        return result

    def parkWeather(self, parkCode) -> str:
        '''Returns weather information of specific park'''
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        data = data[0]
        result = data['weatherInfo']
        return result
    
    def parkDirections(self,parkCode) -> str:
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        data = data[0]
        result = data['directionsInfo']
        return result

    def getParkAlerts(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/alerts?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        result = []
        for alert in data:
            result.append(alert)
        return result
    
    def ifParkAlertsNotZero(self, parkCode) -> bool:
        if len(self.getParkAlerts(parkCode)) > 0:
            result = True
        else:
            result = False
        return result

    def getParkCampgrounds(self, parkCode) -> list:
        pass
        

webApp = NPS(api_key)


