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
        result = ''
        data = data['data']
        data = data[0]
        result = data['description']
        return result
    
    def parkName(self, parkCode):
        '''Returns description of park'''
        r = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        result = ''
        data = data['data']
        data = data[0]
        result = data['name']
        return result

        

webApp = NPS(api_key)

