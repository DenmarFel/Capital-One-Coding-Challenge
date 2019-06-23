import requests
import json

api_key = 'QzrkLi65rTSMTrFTiDGsmdAxWpIpxa72X6JrPEQN'

state = {
    'al':'Alabama',
    'ak':'Alaska',
    'as':'American Samoa',
    'az':'Arizona',
    'ar':'Arkansas',
    'ca':'California',
    'co':'Colorado',
    'ct':'Connecticut',
    'de':'Delaware',
    'dc':'District of Columbia',
    'fl':'Florida',
    'ga':'Georgia',
    'gu':'Guam',
    'hi':'Hawaii',
    'id':'Idaho',
    'il':'Illinois',
    'in':'Indiana',
    'ia':'Iowa',
    'ka':'Kansas',
    'ky':'Kentucky',
    'la':'Loisiana',
    'me':'Maine',
    'md':'Maryland',
    'ma':'Massachusetts',
    'mi':'Michigan',
    'mn':'Minnesota',
    'ms':'Mississippi',
    'mo':'Missouri',
    'mt':'Montana',
    'ne':'Nebraska',
    'nv':'Nevada',
    'nh':'New Hampshire',
    'nj':'New Jersey',
    'nm':'New Mexico',
    'ny':'New York',
    'nc':'North Carolina',
    'nd':'North Dakota',
    'mp':'Northern Mariana Islands',
    'oh':'Ohio',
    'ok':'Oklahoma',
    'or':'Oregon',
    'pa':'Pennsylvania',
    'pr':'Puerto Rico',
    'ri':'Rhode Island',
    'sc':'South Carolina',
    'sd':'South Dakota',
    'tn':'Tennessee',
    'tx':'Texas',
    'ut':'Utah',
    'vt':'Vermont',
    'vi':'Virgin Islands',
    'va':'Virginia',
    'wa':'Washington',
    'wv':'West Virgina',
    'wi':'Wisconsin',
    'wy':'Wyoming'
}

class NPS():

    def __init__(self, api_key: str):
        self._apiKey = api_key
        self._state = state

    def getState(self):
        return self._state

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
        '&fields=images%2Ccontacts%2CentranceFees%2CentrancePasses%2CoperatingHours&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    # Alerts
    def getParkAlerts(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/alerts?parkCode=' + parkCode +
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

    # Campgrounds
    def getCampgroundData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/campgrounds?parkCode=' + parkCode +
        '&fields=fees&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data
    
    # Education: Lesson Plans
    def getLessonData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/lessonplans?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    # People: People
    def getPeopleData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/people?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

    # Events
    def getEventsData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/people?parkCode=' + parkCode +
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

    # Visitor Centers
    def getVisitorcentersData(self, parkCode) -> list:
        r = requests.get('https://developer.nps.gov/api/v1/visitorcenters?parkCode=' + parkCode +
        '&api_key=' + self._apiKey)
        data = r.json()
        data = data['data']
        return data

webApp = NPS(api_key)
        
