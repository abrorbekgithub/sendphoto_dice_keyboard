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
        "text":"Users",
        "reply_markup":{
            "keyboard":[ [{"text":"Users"},{"text":"Orders"}],[{"text":"Welcome Text"},{"text":"Set Logo"}],
            [{"text":"Add Category"},{"text":"Remove Category"}],[{"text":"New Product"},{"text":"Delete Product"}] ],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

reply_markup(ids)