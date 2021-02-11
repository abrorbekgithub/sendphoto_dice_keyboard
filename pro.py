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
        "text":"PRO",
        "reply_markup":{
            "keyboard":[ [{"text":"PRO"}], [{"text":"Mashqlar"},{"text":"So'zlar"},{"text":"Reyting"}],
            [{"text":"Bellashuv"},{"text":"Qo'llanma"}],[{"text":"Sozlamalar"}] ],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

reply_markup(ids)