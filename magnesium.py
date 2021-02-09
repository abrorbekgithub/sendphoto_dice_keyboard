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
        "text":"What's the symbol of Magnesium?\n/A.Mn\n/B.M\n/C.Ma\n/D.Mg",
        "reply_markup":{
            "keyboard":[ [{"text":'A'},{"text":'B'}],[{"text":'C'},{"text":'D'}] ],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

reply_markup(ids)