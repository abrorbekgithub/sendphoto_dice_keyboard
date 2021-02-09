import requests
import json
from pprint import pprint
import os

#1091584118

token=os.environ["TOKEN"]
ids=1091584118


def reply_markup(ids):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":ids,
        "text":"Play With Friends",
        "reply_markup":{
            "keyboard":[ [{"text":"Play With Friends"},{"text":"Trending Games"}],[{"text":"Last PLayed Games"},{"text":"Categories"}],[{"text":"join GAMEE Token Channel"},{"text":"Get App & Win Cash"}] ],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

reply_markup(ids)