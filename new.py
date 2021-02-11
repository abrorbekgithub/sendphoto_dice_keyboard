import requests
import json
import os
from pprint import pprint

token=os.environ["TOKEN"]

def getUpdates():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url=url)
    update=res.json()["result"]
    return update[-1]

def ids():
    ids=getUpdates()["message"]["from"]["id"]
    return ids

