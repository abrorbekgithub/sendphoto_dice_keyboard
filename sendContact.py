import requests
import json
from pprint import pprint
import os

#1091584118

token=os.environ["TOKEN"]
ids=1091584118

def sendContact(ids):
    url=f'https://api.telegram.org/bot{token}/sendContact'
    p={
        "chat_id":ids,
        "phone_number":'998936401030',
        "first_name":'Abrorbek'
    }
    res=requests.get(url,params=p)
    return res.json()

sendContact(ids)