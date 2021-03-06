import json, requests
from datetime import datetime, timedelta
from pytz import timezone

# TODO error catch if no items today

eastern = timezone('US/Eastern')

def getToday():
    fmt = '%Y-%m-%d'
    loc_dt = eastern.localize(datetime.now())
    return loc_dt.strftime(fmt)

def getTomorrow():
    fmt = '%Y-%m-%d'
    dt = datetime.now()
    dt_tom = timedelta(1)

    loc_dt = eastern.localize(dt + dt_tom)
    return loc_dt.strftime(fmt)

def getTime():
    fmt = '%Y-%m-%dT%H:%M:%S'
    loc_dt = eastern.localize(datetime.now())
    return loc_dt.strftime(fmt)

class ItemFormat:
    def __init__(self, name, date):
        self.name = name,
        self.date = date

def parseResponse(response):
    items = []
    for i in range(len(response)):
        name = response[i]['properties']['Name']['title'][0]['text']['content']
        date = response[i]['properties']['Date']['date']['start']

        item = ItemFormat(name, date)
        items.append(item)
    return items


file = open('notionInfo.json')
notionInfo = json.load(file)

# imports integration id and db ids
token = notionInfo['token']
testdb = notionInfo['testdb']
calendardb = notionInfo['calendardb']

file.close()

def getTodayEvents():
    url = f'https://api.notion.com/v1/databases/{calendardb}/query'

    r = requests.post(url, headers={
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2021-08-16"
    }, json={
        'sorts': [
            {
                'property': 'Date',
                'direction': 'descending'
            }
        ],
        'filter': {
            'property': 'Date',
            'date': {
                'equals': getToday(),
                'timezone': 'EST'
            }
        }
    })

    response = r.json()
    response = response['results']
    todayItems = parseResponse(response)

    return todayItems

def getTomorrowEvents():
    url = f'https://api.notion.com/v1/databases/{calendardb}/query'

    r = requests.post(url, headers={
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2021-08-16"
    }, json={
        'sorts': [
            {
                'property': 'Date',
                'direction': 'descending'
            }
        ],
        'filter': {
            'property': 'Date',
            'date': {
                'equals': getTomorrow(),
                'timezone': 'EST'
            }
        }
    })

    response = r.json()
    response = response['results']
    items = parseResponse(response)
    return items
