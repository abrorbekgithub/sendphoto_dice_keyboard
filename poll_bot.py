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
        "text":"Aren't those custom keyboards cool?\n\n/1.Yes,they certainly are\n/2.I'm not quite sure\n/3.No",
        "reply_markup":{
            "keyboard":[[{"text":"Yes,they certainly are"}],[{"text":"I\'m not quite sure"}],[{"text":"No"}]],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

reply_markup(ids)