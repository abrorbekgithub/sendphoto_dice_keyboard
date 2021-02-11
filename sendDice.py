import requests
import json
from pprint import pprint
import os

#1091584118

token=os.environ["TOKEN"]
ids=1091584118


def sendDice(ids):
    url=f'https://api.telegram.org/bot{token}/sendDice'
    p={
        "chat_id":ids,
        # "emoji":"25" ishlamadi
    }
    res=requests.get(url,params=p)
    return res.json()

sendDice(ids)